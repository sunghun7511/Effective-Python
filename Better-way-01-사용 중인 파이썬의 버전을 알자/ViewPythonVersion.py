# -*- coding: utf-8 -*-
'''
## 핵심 정리

* 파이썬의 주요 버전인 파이썬 2, 파이썬 3 모두 여전히 활발히 사용된다.
* 파이썬에서는 CPython, Jython, IronPython, PyPy 같은 다양한 런타임이 있다.
* 시스템에서 파이썬을 실행하는 명령이 사용하고자 하는 파이썬 버전인지 확인해야 한다.
* 파이썬 커뮤니티에서 주로 다루는 버전은 파이썬 3이므로 새 파이썬 프로젝트를 시작할 때는 파이썬 3를 사용하는 편이 좋다.
'''

import sys

print(sys.version_info)
print(sys.version)

'''
shgroup@SH-Group:/mnt/d/Dev/Python/Effective-Python/Better-way-01$ python ViewPythonVersion.py
sys.version_info(major=2, minor=7, micro=12, releaselevel='final', serial=0)
2.7.12 (default, Nov 20 2017, 18:23:56)
[GCC 5.4.0 20160609]
shgroup@SH-Group:/mnt/d/Dev/Python/Effective-Python/Better-way-01$ python3 ViewPythonVersion.py
sys.version_info(major=3, minor=5, micro=2, releaselevel='final', serial=0)
3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609]
shgroup@SH-Group:/mnt/d/Dev/Python/Effective-Python/Better-way-01$
'''