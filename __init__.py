bl_info = {
	"name": "MMD to PES",
	"category": "Rigging",
	"author": "MFG",
	"version": "0.0.2"
}

import bpy, fnmatch, builtins

logfile = open('mmd_debug.txt', 'w', encoding='utf-16')

def print(*args):
    builtins.print(args, file=logfile)
    logfile.flush()

def doTheThing(context, booba_factor=False):
	obj = context.active_object

	remap = {
		"上半身": "sk_belly",
		"上半身2": "sk_chest",
		"下半身": "dsk_hip",
		"首": "sk_neck",
		"頭": "sk_head",
		"肩.R": "sk_shoulder_r",
		"腕.R": "dsk_upperarm_r",
		"腕捩.R": "sk_upperarm_r",
		"ひじ.R": "sk_forearm_r",
		"手捩.R": "dsk_forearm_r",
		"手首.R": "sk_hand_r",
		"足.R": "sk_thigh_r",
		"足D.R": "sk_thigh_r",
		"ひざ.R": "sk_leg_r",
		"ひざD.R": "sk_leg_r",
		"すね.R": "sk_leg_r",
		"足首.R": "sk_foot_r",
		"足首D.R": "sk_foot_r",
		"足先EX.R": "dsk_toe_r",
		"つま先.R": "dsk_toe_r",
		"肩.L": "sk_shoulder_l",
		"腕.L": "dsk_upperarm_l",
		"腕捩.L": "sk_upperarm_l",
		"ひじ.L": "sk_forearm_l",
		"手捩.L": "dsk_forearm_l",
		"手首.L": "sk_hand_l",
		"足.L": "sk_thigh_l",
		"足D.L": "sk_thigh_l",
		"ひざ.L": "sk_leg_l",
		"ひざD.L": "sk_leg_l",
		"すね.L": "sk_leg_l",
		"足首.L": "sk_foot_l",
		"足首D.L": "sk_foot_l",
		"足先EX.L": "dsk_toe_l",
		"つま先.L": "dsk_toe_l",
		"小指１.R": "skh_pinky_mcp_r",
		"小指２.R": "skh_pinky_pip_r",
		"小指３.R": "skh_pinky_dip_r",
		"薬指１.R": "skh_ring_mcp_r",
		"薬指２.R": "skh_ring_pip_r",
		"薬指３.R": "skh_ring_dip_r",
		"中指１.R": "skh_middle_mcp_r",
		"中指２.R": "skh_middle_pip_r",
		"中指３.R": "skh_middle_dip_r",
		"人指１.R": "skh_index_mcp_r",
		"人指２.R": "skh_index_pip_r",
		"人指３.R": "skh_index_dip_r",
		"小指１.L": "skh_pinky_mcp_l",
		"小指２.L": "skh_pinky_pip_l",
		"小指３.L": "skh_pinky_dip_l",
		"薬指１.L": "skh_ring_mcp_l",
		"薬指２.L": "skh_ring_pip_l",
		"薬指３.L": "skh_ring_dip_l",
		"中指１.L": "skh_middle_mcp_l",
		"中指２.L": "skh_middle_pip_l",
		"中指３.L": "skh_middle_dip_l",
		"人指１.L": "skh_index_mcp_l",
		"人指２.L": "skh_index_pip_l",
		"人指３.L": "skh_index_dip_l",
		"腕捩1.R": "dsk_upperarm_r",
		"腕捩2.R": "sk_upperarm_r",
		"腕捩3.R": "sk_upperarm_r",
		"手捩1.R": "sk_forearm_r",
		"手捩2.R": "sk_forearm_r",
		"手捩3.R": "dsk_forearm_r",
		"腕捩1.L": "dsk_upperarm_l",
		"腕捩2.L": "sk_upperarm_l",
		"腕捩3.L": "sk_upperarm_l",
		"手捩1.L": "sk_forearm_l",
		"手捩2.L": "sk_forearm_l",
		"手捩3.L": "dsk_forearm_l",
		"胸上2.L": "sk_chest",
		"胸上2.R": "sk_chest",
		"LeftBreast": "breast_l",
		"RightBreast": "breast_r",
		"目.L": "sk_head",
		"目.R": "sk_head",
		"舌1": "sk_head",
		"舌2": "sk_head",
		"ムカッ": "sk_head",
		"汗": "sk_head",
		"目戻.R": "sk_head",
		"目戻.L": "sk_head"
	}

	wildcard_mix = {
		"胸*.L": "breast_l",
		"胸*.R": "breast_r",
	}

	delete_list = [
		"mmd_edge_scale",
		"mmd_vertex_order"
	]

	mix_to = {}

	#check for zero-indexed thumbs
	thumbs_zero_indexed = False
	for vg in obj.vertex_groups:
		if vg.name.startswith('親指０'):
			thumbs_zero_indexed = True
			break
		elif vg.name.startswith('親指３'):
			break

	if thumbs_zero_indexed:
		remap["親指０.R"] = "skh_thumb_mata_r"
		remap["親指１.R"] = "skh_thumb_mcp_r"
		remap["親指２.R"] = "skh_thumb_pip_r"
		remap["親指０.L"] = "skh_thumb_mata_l"
		remap["親指１.L"] = "skh_thumb_mcp_l"
		remap["親指２.L"] = "skh_thumb_pip_l"
	else:
		remap["親指１.R"] = "skh_thumb_mata_r"
		remap["親指２.R"] = "skh_thumb_mcp_r"
		remap["親指３.R"] = "skh_thumb_pip_r"
		remap["親指１.L"] = "skh_thumb_mata_l"
		remap["親指２.L"] = "skh_thumb_mcp_l"
		remap["親指３.L"] = "skh_thumb_pip_l"

	print("thumbs_zero_indexed: "+str(thumbs_zero_indexed))

	#populate mix_to with the first match for a VG remap or existing remapped VGs
	for vg in obj.vertex_groups:
		if vg.name in remap:
			new_name = remap[vg.name]
			if not new_name in mix_to:
				vg.name = new_name
				mix_to[new_name] = vg
		elif vg.name in remap.values():
			mix_to[vg.name] = vg

	def print_mix_to():
		s = "mix_to = {\n"
		for key in mix_to.keys():
			s += "\t\"" + key + "\": \"" + mix_to[key].name + ",\n"
		s += "}\n"
		print(s)

	def delete_and_normalize(vg):
		print('Removing '+vg.name)
		obj.vertex_groups.remove(vg)
		bpy.ops.object.vertex_group_normalize_all()

	def weight_mix(a, b, weight=1.0, delete=True):
		print('Mixing '+b.name+' to '+a.name)
		mod = obj.modifiers.new('Vertex Weight Mix', 'VERTEX_WEIGHT_MIX')
		mod.vertex_group_a = a.name
		mod.vertex_group_b = b.name
		mod.mix_mode = 'ADD'
		mod.mix_set = 'ALL'
		mod.mask_constant = weight
		bpy.ops.object.modifier_apply(modifier=mod.name)
		if delete: delete_and_normalize(b)

	def get_in_mix(vg):
		if vg.name in remap: return mix_to[remap[vg.name]]
		return None

	def wildcard_match(vg):
		for pattern, to in wildcard_mix.items():
			if fnmatch.fnmatch(vg.name, pattern):
				return mix_to[wildcard_mix[pattern]]
		return None

	#delete VGs
	for vg in obj.vertex_groups:
		if vg.name in delete_list:
				delete_and_normalize(vg)

	#remap VGs
	for vg in obj.vertex_groups:
		if not vg.name in remap.values():
			to = get_in_mix(vg)
			if to is None:
				to = wildcard_match(vg)
			if to is not None:
				weight_mix(to, vg)

	#create breast movement or mix it back to sk_chest
	if 'breast_l' in mix_to:
		if booba_factor != False:
			weight_mix(mix_to['sk_chest'], mix_to['breast_l'], weight=(1-booba_factor), delete=False)
			weight_mix(mix_to['sk_thigh_l'], mix_to['breast_l'], weight=booba_factor)
			weight_mix(mix_to['sk_chest'], mix_to['breast_r'], weight=(1-booba_factor), delete=False)
			weight_mix(mix_to['sk_thigh_r'], mix_to['breast_r'], weight=booba_factor)
		else:
			weight_mix(mix_to['sk_chest'], mix_to['breast_l'])
			weight_mix(mix_to['sk_chest'], mix_to['breast_r'])

	bpy.ops.object.vertex_group_remove_unused()

class MMDtoPES(bpy.types.Operator):
	"""Convert vertex groups from MMD to PES"""
	bl_idname = "object.mmd_to_pes"
	bl_label = "PESify MMD vertex groups"
	bl_options = {'REGISTER', 'UNDO'}

	def execute(self, context):
		doTheThing(context)

		return {'FINISHED'}

class MMDtoPESformaDeHorny(bpy.types.Operator):
	"""Convert vertex groups from MMD to PES"""
	bl_idname = "object.mmd_to_pes_boobies"
	bl_label = "PESify MMD vertex groups (w/ Booby Jiggles)"
	bl_options = {'REGISTER', 'UNDO'}

	booba_factor = bpy.props.FloatProperty(name = "Booba Factor", min = 0.0, max = 1.0, default = 0.1, description="Amount of weight to assign to sk_thigh_l/r, values larger than 0.2 are probably retarded")

	def execute(self, context):
		doTheThing(context, booba_factor=self.booba_factor)

		return {'FINISHED'}

def register():
	bpy.utils.register_class(MMDtoPES)
	bpy.utils.register_class(MMDtoPESformaDeHorny)

def unregister():
	bpy.utils.unregister_class(MMDtoPES)
	bpy.utils.unregister_class(MMDtoPESformaDeHorny)

if __name__ == "__main__":
	register()

