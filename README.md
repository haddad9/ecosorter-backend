# Bangkit Team C23-PR536, EcoSorter

Product-based Capstone Bangkit Academy 2023
--
# Members:
1. Machine Learning:
- Aloysius Darin Ario (M151DSX1837) – Universitas Brawijaya
- M.Farhan Zachary (M312DKX4604) – Indonesia Defense University
- Wintang Dayinta Wiyanto (M013DSY2108) – Institut Pertanian Bogor

2. Cloud Computing:
- Andhika Rifki Alfariz (C181DSX1965) – Universitas Indonesia
- Muhammad Haddad (C181DSX0964) – Universitas Indonesia

3. Mobile Development:
- Bimabara Sukma Muryanto (A181DSX1228) – Universitas  Indonesia

Final Selected Themes:
--
Sustainable Living

Title of the Project: 
--
EcoSorter

Summary of Project: 
--
Our project aims to tackle the growing Indonesia problem of waste management and disposal by developing a mobile application that classifies waste items and educates users on proper waste management practices. The application leverages image processing and machine learning algorithms to identify and categorize waste materials, followed by providing relevant articles and guidelines to help users dispose of the waste responsibly. By addressing the lack of knowledge and awareness surrounding waste management, we aim to encourage responsible waste disposal behavior, contributing to a cleaner environment.

Step to Replicate : 
--

1. Machine Learning:
- Dataset (from Kaggle)
- Feature exploration
- Preprocessing (scaling, normalization, data augmentation)
- Define deep learning model using TensorFlow 
- Hyperparameter tuning 
- Save and load model to evaluate model performance

2. Mobile Development:
- Design UI layout (optional: Figma)
- Dependencies (see Technology used part)
- Navigation
- Connecting local database to UI (using ViewModel, Room, optional: Flow, Koin, Clean Architecture)
- Implement external feature (accessing camera)
- Connecting to remote (using Firestore for database and Firebase storage for file)
- Implement machine learning using TFLite

3. Cloud Computing:
- Create a project on Google Cloud Platform
- Set default region as asia-southeast2(Jakarta)
> go to gcp console and write this command : $gcloud config set compute/region asia-southeast2
- Create a project on Firebase
- Create storage with records and profile folders
- Cloud Storage Browser page
  - Create bucket
  - Name your bucket : "-----"
  - Location type : region
  - Choose where to store your data = asia-southeast2
  - Leave the default setting
  - create
- Create a firestore for the database 

Technology Used : 
--
- [Firebase](https://firebase.google.com)
- [TensorFlow](https://www.tensorflow.org/lite/guide/android)
- [Keras]([https://keras.io/])
- [Google Cloud Platform](https://cloud.google.com/gcp)

Project Resources : 
--
### Budget
Google Cloud Platform Subscription : **$200**

### Dataset:
- [Non and Biodegradable Material Dataset](https://www.kaggle.com/datasets/rayhanzamzamy/non-and-biodegradable-waste-dataset)

### Paper / Journals / articles:
- [Identifikasi Penyakit pada Daun Kopi Menggunakan Metode Deep Learning VGG16](https://jurnal.yudharta.ac.id/v2/index.php/EXPLORE-IT/article/view/2689)

### Design Apps :
[Design](https://www.figma.com/file/j81lA9sBapgNRp8tfqKYZG/Kerani-(Kerabat-Tani)?node-id=0%3A1)

### Deployment of The Server and ML Model to Google Cloud Platform
#### 1. Create Firewall Rule. Navigation Menu >VPC Network >Firewall
Firewall rules control incoming or outgoing traffic to an instance. Here are the steps to create firewall rule for this project.
Click create firewall rule. Specified target tags and fill the source IPv4 ranges with 0.0.0.0/0. Specified TCP port to 8080. Then create.
#### 2. Create VM instance in Compute Engine. VM instance is where we deploy our server
Click create VM instance. Choose to allow http. Enter the network tags that we created in the firewall rule. Then create.
#### 3. Run command in SSH.
##### Update
  - sudo apt update
##### Install git
  - sudo apt install git
##### Clone our repository
  - git clone https://github.com/Rian214/c22-ps164-kerani.git
##### Install wget downloading files from web or FTP servers
  - sudo apt install wget
##### Install minoconda to get python environment.
  - wget https://repo.anaconda.com/miniconda/Miniconda3-4.7.10-Linux-x86_64.sh
  - bash Miniconda3-4.7.10-Linux-x86_64.sh
##### Point to your path, confirm the instalation, create, and activate the environment.
  - export PATH=/home/<your folder name>/miniconda3/bin:$PATH
  - which conda
  - conda create -n c22-ps164-kerani python=3.7
  - conda activate c22-ps164-kerani
  - conda init
##### Get into the directory
  - cd c22-ps164-kerani
  - cd backend
##### Install all the libraries
  - python3 -m pip install firebase_admin
  - python3 -m pip install pyrebase4
  - python3 -m pip install flask
  - python3 -m pip install tensorflow
  - python3 -m pip install numphy
  - python3 -m pip install image
  - python3 -m pip install keras
  - python3 -m pip install Keras-Preprocessing
  - python3 -m pip install matplotlib
  - python3 -m pip install numpy
  - python3 -m pip installpandas
  - python3 -m pip installPillow
  - python3 -m pip install requests
  - python3 -m pip install scipy==1.8.1
  - python3 -m pip install h5py
##### Make directory for ML Model and upload ML Model
  - mkdir Asset
##### Run the server
  - python3 app.py
  