import os
from  functionality import *
while True:
 os.system("clear")
 print("--------------------------------------------WelCome To Menu Drive Program of LVM-----------------------------------------------------------------")
 print("Press the Number Correponding to the choice")
 print('''1. For Creating PV
2. For Removing PV
3. For Creating VG
4. For extending VG
5. For Reducing VG
6. For Removing VG
7. For Creating LV
8. For Extending LV
9. For Reducing LV
10.For Deleting LV
11.For Exit ''')
 val=int(input("Enter ur choice-: "))
 if val ==1 :
     pv_name=input("Enter the name of the partition(provide absolute path eg. /dev/sda -: ")
     add_pv(pv_name)

 elif val ==2 :
     pv_name=input("Enter the name of the PV eg. /dev/sda -: ")
     remove_pv(pv_name)

 elif val==3 :
     vg_name=input("Enter the name u want to give to VG -: ")
     pv_name=input("Enter the name of one pv u want to associate with vg -: ")
     create_vg(vg_name,pv_name)

 elif val ==4 :
     vg_name=input("Enter the name of  VG u want to extend -: ")
     pv_name=input("Enter the name of  pv u want to associate with vg -: ")
     extend_vg(vg_name,pv_name)


 elif val==5 :
     vg_name=input("Enter the name of  VG u want to reduce -: ")
     pv_name=input("Enter the name of  pv u want to remove from  vg -: ")
     reduce_vg(vg_name,pv_name)

 elif val==6 :
     vg_name=input("Enter the name of the VG -: ")
     remove_vg(vg_name)

 elif val==7 :
     vg_name=input("Enter the name of vg from which u want to take volume for lvm -: ")
     lv_name=input("Enter the name u want to give to the lvm -: ")
     size=input("Enter the size of lvm -: ")
     create_lv(vg_name,lv_name,size)

 elif val==8:
     lv_name=input("Enter the name of LVM (in absolute path like  /dev/<vg-name>/<lvm-name> ")
     size=input("Enter the final size u want to provide to LVM")
     extend_lv(lv_name,size)

 elif val==9:
     lv_name=input("Enter the name of LVM (in absolute path like  /dev/<vg-name>/<lvm-name>) ")
     size=input("Enter the final size u want to provide to LVM")
     reduce_lv(lv_name,size)
 
 elif val ==10 :
     lv_name=input("Enter the name of the LVM (in absolute path like  /dev/<vg-name>/<lvm-name>) -: ")
     remove_lv(lv_name)

 elif val==11:
     exit()
 else :
     print("Wrong Input..:( ")
 input("Press Any Key To Continue ...")
 os.system("clear")
