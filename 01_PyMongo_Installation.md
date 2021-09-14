## mongo-python-driver (aka PyMongo)

---

###### Install all following packages as "root" user

Extra Packages for Enterprise Linux (EPEL) are required : verify and install :
```
rpm -qa | grep epel
yum install epel-release
```

<br><br>

Package manager for Python (PIP) is required : verify and install :
```
rpm -qa | grep pip
yum install python-pip
```

<br><br>

Install PyMongo :
```
python -m pip install 'pymongo[srv]'
```

---

###### sample output :

```
[root@oramad.OracleByExample.com ~]# python -m pip install 'pymongo[srv]'
Collecting pymongo[srv]
  Downloading https://files.pythonhosted.org/packages/85/9a/f6e9a047d8b03a246c7a6fbf6bccd060dc4b2fe44a961e0f5f51ce9e4cbd/pymongo-3.12.0-cp36-cp36m-manylinux1_x86_64.whl (506kB)
    100% |--------------------------------| 512kB 2.6MB/s
Collecting dnspython<2.0.0,>=1.16.0; extra == "srv" (from pymongo[srv])
  Downloading https://files.pythonhosted.org/packages/ec/d3/3aa0e7213ef72b8585747aa0e271a9523e713813b9a20177ebe1e939deb0/dnspython-1.16.0-py2.py3-none-any.whl (188kB)
    100% |--------------------------------| 194kB 6.5MB/s
Installing collected packages: dnspython, pymongo
Successfully installed dnspython-1.16.0 pymongo-3.12.0
[root@oramad.OracleByExample.com ~]#
```
---

