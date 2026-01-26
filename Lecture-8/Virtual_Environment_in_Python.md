# Creat Env in (\C:) Directory

```python
conda create -n {Environment Name} python={Python Version} -y
```
```python
conda activate {Environment Name}
```
```python
conda env list
```
```python
conda remove --name {Environment Name} --all
```

---

# Creat Env in another Directory

```python
conda create --prefix .\{Environment Name} python={Python Version} -y
```
```python
conda activate .\{Environment Name}
```

---

# Install a Python Package by Command

```python
pip install {Library Name}=={Library Version}
```

---