# About :
Names Generator is a python package that draws your name in the console with custom symbols and sizes easily and in one line

# images :

![image1](https://github.com/AbdulrhmanSayedAli/NamesGenerator/blob/main/images/image_1.png)

![image2](https://github.com/AbdulrhmanSayedAli/NamesGenerator/blob/main/images/image_2.png)

![image3](https://github.com/AbdulrhmanSayedAli/NamesGenerator/blob/main/images/image_3.png)


# usage :
install the library using this command in the cmd

```python
pip install -i https://test.pypi.org/simple/ NamesGeneratorByRoctes7
```



# there is three modes in this package :

* DrawWithYourNameLettersMode : generates your name with your name's letters


```python
import NamesGeneratorByRoctes7 as e
e.DrawWithYourNameLettersMode("sarah")
```


* DrawWithCustomSize : generates your name with custom size

```python
import NamesGeneratorByRoctes7 as e
e.DrawWithCustomSize("AA" ,"#" , 30)
```
<b> Note : </b> size should be divisible by five

* DrawWithRandomMode : generates your name with a random symbols defined by you

```python
import NamesGeneratorByRoctes7 as e
e.DrawWithRandomMode("tony" , ["0","1"])
```