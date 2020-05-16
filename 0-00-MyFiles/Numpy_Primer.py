"E:\Python 3.8.0\python.exe" "C:\Program Files\JetBrains\PyCharm Community Edition 2019.1.1\plugins\python-ce\helpers\pydev\pydevconsole.py" --mode=client --port=50007

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['F:\\PythonCodes-PlotlyDash', 'F:/PythonCodes-PlotlyDash'])

Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.11.1 -- An enhanced Interactive Python. Type '?' for help.
PyDev console: using IPython 7.11.1

Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
In[2]: import numpy as np
In[3]: mylist = range(1,10)
In[4]: mylist
Out[4]: range(1, 10)
In[5]: arr = np.array(mylist)
In[6]: arr
Out[6]: array([1, 2, 3, 4, 5, 6, 7, 8, 9])
In[7]: type(arr)
Out[7]: numpy.ndarray
In[8]: arr = np.arange(1, 10)
In[9]: arr
Out[9]: array([1, 2, 3, 4, 5, 6, 7, 8, 9])
In[10]: arr = np.arange(1, 10, 2)
In[11]: arr
Out[11]: array([1, 3, 5, 7, 9])
In[12]: np.zeros((5, 4))
Out[12]:
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
In[13]: arr = np.ones((5, 4))
In[14]: arr
Out[14]:
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
In[15]: # Uniform distribution
In[16]: arr = np.random.randint(100)
In[17]: arr
Out[17]: 32
In[18]: arr = np.random.randint(100)
In[19]: arr
Out[19]: 2
In[20]: arr = np.random.randint(0, 100)
In[21]: arr
Out[21]: 80
In[22]: arr = np.random.randint(0, 100, (2, 5))
In[23]: arr
Out[23]:
array([[56, 27,  0, 17, 40],
       [66, 46,  9, 79, 17]])
In[24]: # Linearly spaced values
In[25]: arr = np.linspace(0, 10)
In[26]: arr
Out[26]:
array([ 0.        ,  0.20408163,  0.40816327,  0.6122449 ,  0.81632653,
        1.02040816,  1.2244898 ,  1.42857143,  1.63265306,  1.83673469,
        2.04081633,  2.24489796,  2.44897959,  2.65306122,  2.85714286,
        3.06122449,  3.26530612,  3.46938776,  3.67346939,  3.87755102,
        4.08163265,  4.28571429,  4.48979592,  4.69387755,  4.89795918,
        5.10204082,  5.30612245,  5.51020408,  5.71428571,  5.91836735,
        6.12244898,  6.32653061,  6.53061224,  6.73469388,  6.93877551,
        7.14285714,  7.34693878,  7.55102041,  7.75510204,  7.95918367,
        8.16326531,  8.36734694,  8.57142857,  8.7755102 ,  8.97959184,
        9.18367347,  9.3877551 ,  9.59183673,  9.79591837, 10.        ])
In[27]: arr = np.linspace(0, 10, 5)
In[28]: arr
Out[28]: array([ 0. ,  2.5,  5. ,  7.5, 10. ])
In[29]: np.random.seed(101)
In[30]: arr = np.random.randint(0, 100, 10)
In[31]: arr
Out[31]: array([95, 11, 81, 70, 63, 87, 75,  9, 77, 40])
In[32]: arr = np.random.randint(0, 100, 10)
In[33]: arr
Out[33]: array([ 4, 63, 40, 60, 92, 64,  5, 12, 93, 40])
In[34]: np.random.seed(101)
In[35]: arr = np.random.randint(0, 100, 10)
In[36]: arr
Out[36]: array([95, 11, 81, 70, 63, 87, 75,  9, 77, 40])
In[37]: arr.max()
Out[37]: 95
In[38]: arr.min()
Out[38]: 9
In[39]: arr.mean()
Out[39]: 60.8
In[40]: arr.argmax()
Out[40]: 0
In[41]: arr.argmin()
Out[41]: 7
In[42]: arr.resize(2, 5)
In[43]: arr
Out[43]:
array([[95, 11, 81, 70, 63],
       [87, 75,  9, 77, 40]])
In[44]: arr.reshape(2, 5)
Out[44]:
array([[95, 11, 81, 70, 63],
       [87, 75,  9, 77, 40]])
In[45]: a = np.array([[0, 1], [2, 3]], order='C')
In[46]: a
Out[46]:
array([[0, 1],
       [2, 3]])
In[47]: a.resize((2, 1))
Traceback (most recent call last):
  File "C:\Users\Niloy\AppData\Roaming\Python\Python38\site-packages\IPython\core\interactiveshell.py", line 3319, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-47-81e4f4aed5e6>", line 1, in <module>
    a.resize((2, 1))
ValueError: cannot resize an array that references or is referenced
by another array in this way.
Use the np.resize function or refcheck=False
In[48]: import sys
In[49]: sys.getrefcount(a)
Out[49]: 8
In[50]: del arr
In[51]: sys.getrefcount(a)
Out[51]: 8
In[52]: a.resize(refcheck = false)
Traceback (most recent call last):
  File "C:\Users\Niloy\AppData\Roaming\Python\Python38\site-packages\IPython\core\interactiveshell.py", line 3319, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-52-ded1771ad894>", line 1, in <module>
    a.resize(refcheck = false)
NameError: name 'false' is not defined
In[53]: a.resize(refcheck = False)
In[54]: a
Out[54]:
array([[0, 1],
       [2, 3]])
In[55]: a.resize((2, 1), refcheck = False)
In[56]: a
Out[56]:
array([[0],
       [1]])
In[57]: a = np.array([[0, 1], [2, 3]], order='R')
Traceback (most recent call last):
  File "C:\Users\Niloy\AppData\Roaming\Python\Python38\site-packages\IPython\core\interactiveshell.py", line 3319, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-57-8ca0683a1f1f>", line 1, in <module>
    a = np.array([[0, 1], [2, 3]], order='R')
TypeError: order not understood
In[58]: a = np.array([[0, 1], [2, 3]], order='F')
In[59]: a
Out[59]:
array([[0, 1],
       [2, 3]])
In[60]: a.resize(1,1)
Traceback (most recent call last):
  File "C:\Users\Niloy\AppData\Roaming\Python\Python38\site-packages\IPython\core\interactiveshell.py", line 3319, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-60-4efa3cbe15ef>", line 1, in <module>
    a.resize(1,1)
ValueError: cannot resize an array that references or is referenced
by another array in this way.
Use the np.resize function or refcheck=False
In[61]: a.resize(1,1, refcheck = False)
In[62]: a
Out[62]: array([[0]])
In[63]: a.resize(1,2, refcheck = False)
In[64]: a
Out[64]: array([[0, 0]])
In[65]: a.resize(2,3, refcheck = False)
In[66]: a
Out[66]:
array([[0, 0, 0],
       [0, 0, 0]])
In[67]: a = np.array([[0, 1], [2, 3]], order='R')
Traceback (most recent call last):
  File "C:\Users\Niloy\AppData\Roaming\Python\Python38\site-packages\IPython\core\interactiveshell.py", line 3319, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-67-8ca0683a1f1f>", line 1, in <module>
    a = np.array([[0, 1], [2, 3]], order='R')
TypeError: order not understood
In[68]: a = np.array([[0, 1], [2, 3]], order='C')
In[69]: a.resize(2,3, refcheck = False)
In[70]: a
Out[70]:
array([[0, 1, 2],
       [3, 0, 0]])
In[71]: mat = np.arange(0, 50).reshape(5, 10)
In[72]: mat
Out[72]:
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]])
In[73]: mat[2,3]
Out[73]: 23
In[74]: mat[2:,3]
Out[74]: array([23, 33, 43])
In[75]: mat > 35
Out[75]:
array([[False, False, False, False, False, False, False, False, False,
        False],
       [False, False, False, False, False, False, False, False, False,
        False],
       [False, False, False, False, False, False, False, False, False,
        False],
       [False, False, False, False, False, False,  True,  True,  True,
         True],
       [ True,  True,  True,  True,  True,  True,  True,  True,  True,
         True]])
In[76]: mat[mat > 35]
Out[76]: array([36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49])

