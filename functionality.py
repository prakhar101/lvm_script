import os
import subprocess
def add_pv(part_name) :
    out=subprocess.run("pvcreate {} ".format(part_name),shell=True,stdout=subprocess.PIPE,input=b'y\n')
    if out.returncode == 0:
        print("PV Created Sucessfully!!!")
    else :
        print("OOPS !! Some Error occured")
        print(out.stderr)


def remove_pv(part_name) :
    out=subprocess.run("pvremove {} ".format(part_name),shell=True,stdout=subprocess.PIPE,input=b'y\n')
    if out.returncode == 0:
        print("PV removed Sucessfully!!!")
    else :
        print("OOPS !! Some Error occured")
        print(out.stderr)


def create_vg(vg_name,pv_name) :
    out=subprocess.run("vgcreate {0} {1}".format(vg_name,pv_name))
    if out.returncode==0 :
        print("VG created successfully")
    else :
        print("OOPs !! Some error occured")
        print(out.stderr)


def extend_vg(vg_name,pv_name) :
    out=subprocess.run("vgextend {0} {1} ".format(vg_name,pv_name),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if out.returncode ==0 :
        print("Vgextend Successfully!!!")
    else :
        print("OOPS !!Some error occured")
        print(out.stderr)


def reduce_vg(vg_name,pv_name) :
    out=subprocess.run("vgreduce {0} {1} ".format(vg_name,pv_name),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,input=b'y\n')
    if out.returncode ==0 :
        print("Vgreduce Successfully!!!")
    else :
        print("OOPS !!Some error occured")
        print(out.stderr)

def remove_vg(vg_name) :
    os.system("vgremove {}".format(vg_name))


def create_lv(vg_name,lv_name,size) :
    out=subprocess.run("lvcreate --name {0} --size {1} {2}".format(lv_name,size,vg_name),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if out.returncode ==0 :
        print("lv created  Successfully!!!")
    else :
        print("OOPS !!Some error occured")
        print(out.stderr)

def remove_lv(lv_name) :
    out=subprocess.run("lvremove {}".format(lv_name),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,input=b'y\n')
    if out.returncode ==0 :
        print("lv removed  Successfully!!!")
    else :
        print("OOPS !!Some error occured")
        print(out.stderr)

def extend_lv(lv_name,size) :
    out=subprocess.run("lvextend {} --size {}".format(lv_name,size),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,input=b'y\n')
    if out.returncode ==0 :
        subprocess.run("e2fsck -f {}".format(lv_name),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        subprocess.run("resize2fs lv_name",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print("LV extended Successfully!!!")
    else :
        print("OOPS !!Some error occured")
        print(out.stderr)


def reduce_lv(lv_name,size) :
    subprocess.run("e2fsck -f {}".format(lv_name),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    subprocess.run("resize2fs {} {}".format(lv_name,size),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out=subprocess.run("lvreduce {} --size {}".format(lv_name,size),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,input=b'y\n')
    if out.returncode ==0 :
        print("LV reduced  Successfully!!!")
    else :
        print("OOPS !!Some error occured")
        print(out.stderr)

