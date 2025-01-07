Dev: (require cmake)
```
pip install setuptools pillow face_recognition git+https://github.com/ageitgey/face_recognition_models
pip install 
```

Docker
```
docker build -t whereme .
```
powershell:
```
docker run --rm -it -v ${pwd}:/whereme -e ME=/whereme/me.png -e IN=/whereme/in -e OUT=/whereme/out whereme
```
bash:
```
docker run --rm -it -v `pwd`:/whereme -e ME=/whereme/me.png -e IN=/whereme/in -e OUT=/whereme/out whereme
```
Load image:
```
docker load -i whereme.tar
```
