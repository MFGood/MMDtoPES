# MMDtoPES
Blender addon to convert MMD vertex groups to PES ones

Made to be used with MMD models imported into [Blender 2.79](https://www.blender.org/download/releases/2-79/) with [MMD Tools](https://github.com/powroupi/blender_mmd_tools) for use with [PES FMDL Blender](https://github.com/the4chancup/pes-fmdl-blender)

# Installation
Grab the .zip file from [releases](https://github.com/MFGood/MMDtoPES/releases/latest) and navigate to File -> User Preferences:<br>
![image](https://user-images.githubusercontent.com/98861097/199644934-b1497343-be3d-4716-9a0a-dce3c087cb38.png)<br>
Then click "Install Add-on from File..." and select MMDtoPES.\<version\>.zip:<br>
![image](https://user-images.githubusercontent.com/98861097/199645002-8f97f628-22f6-4c16-ae79-38e2d27fb657.png)<br>
Navigate to downloads and search "MMD" in the top right to find it more easily:
![image](https://user-images.githubusercontent.com/98861097/199645262-fffc5d23-c2f5-40b9-bc67-2f6fad1dfbbe.png)

# Usage
If you don't have the ability to import MMD models, install [MMD Tools](https://github.com/powroupi/blender_mmd_tools). Then, simply select the option from the menu like so:<br>
![image](https://user-images.githubusercontent.com/98861097/217376311-16ea798c-4364-4f49-af1b-f9bea5eafaee.png)<br>
Then, import a PES reference model and scale the MMD down around it. However, before you can begin posing as normal, there's a few things you might have to do. First, if there's anything unnecessary in the scene, you can get rid of it by doing a right click -> Delete Hierarchy:<br>
![image](https://user-images.githubusercontent.com/98861097/217377345-d184e4b3-1586-41d8-9b23-4c5dac1bde37.png)<br>
Second, you may find that if you try to pose the skeleton in certain places like the legs, the bones are yellow and don't move as normal:<br>
![image](https://user-images.githubusercontent.com/98861097/217377569-af695a15-6d64-4df5-a772-39908053d076.png)<br>
To fix this, select the bone and then go to the bone constraints tab in the right panel and just click all the X's:<br>
![image](https://user-images.githubusercontent.com/98861097/217377962-730a0a2a-7348-48e7-99c6-cad7a7f14813.png)<br>
Repeat this on any other bones as needed.
Third, you may find that when you move the skeleton the mesh doesn't move also. To fix this, you need to assign the skeleton as an armature modifier:<br>
![image](https://user-images.githubusercontent.com/98861097/217378358-6fcee8cc-9b5c-4930-acf8-bdb7441a5706.png)<br>
*NOTE: do not click apply just yet*<br><br>
From there, go about posing your model as normal, then when it comes time to rename and mix weights on vertex groups, press Space and run this instead:<br>
![image](https://user-images.githubusercontent.com/98861097/199641629-add93020-67f6-4f3d-be0e-cf4855509ad4.png)<br>
*Except it'll say "PESify MMD vertex groups"*<br><br>
Assigns all face and head groups to the sk_head group; hair and head accessories must still be manually assigned. Also reassigns hand groups; hands must be separated out into separate meshes and exported as separate models to properly function. Any other non-standard vertex groups (accessories, tails, animal ears etc.) may need to be manually assigned.

Booby Jiggles version assigns weight of each boob to the motion of the thigh by 0.1 by default, though you can configure this in the panel in the bottom right:<br>
![image](https://user-images.githubusercontent.com/98861097/217380270-02b5a4b6-fce9-439a-b210-8f072385e486.png)<br>
