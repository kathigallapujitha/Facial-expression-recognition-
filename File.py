Collecting fer
  Downloading fer-22.5.1-py3-none-any.whl.metadata (6.4 kB)
Requirement already satisfied: opencv-python-headless in /usr/local/lib/python3.12/dist-packages (4.12.0.88)
Requirement already satisfied: matplotlib in /usr/local/lib/python3.12/dist-packages (from fer) (3.10.0)
Requirement already satisfied: opencv-contrib-python in /usr/local/lib/python3.12/dist-packages (from fer) (4.12.0.88)
Requirement already satisfied: keras>=2.0.0 in /usr/local/lib/python3.12/dist-packages (from fer) (3.10.0)
Requirement already satisfied: pandas in /usr/local/lib/python3.12/dist-packages (from fer) (2.2.2)
Requirement already satisfied: requests in /usr/local/lib/python3.12/dist-packages (from fer) (2.32.4)
Collecting facenet-pytorch (from fer)
  Downloading facenet_pytorch-2.6.0-py3-none-any.whl.metadata (12 kB)
Requirement already satisfied: tqdm>=4.62.1 in /usr/local/lib/python3.12/dist-packages (from fer) (4.67.1)
Requirement already satisfied: moviepy in /usr/local/lib/python3.12/dist-packages (from fer) (1.0.3)
Collecting ffmpeg==1.4 (from fer)
  Downloading ffmpeg-1.4.tar.gz (5.1 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: Pillow in /usr/local/lib/python3.12/dist-packages (from fer) (11.3.0)
Requirement already satisfied: numpy<2.3.0,>=2 in /usr/local/lib/python3.12/dist-packages (from opencv-python-headless) (2.0.2)
Requirement already satisfied: absl-py in /usr/local/lib/python3.12/dist-packages (from keras>=2.0.0->fer) (1.4.0)
Requirement already satisfied: rich in /usr/local/lib/python3.12/dist-packages (from keras>=2.0.0->fer) (13.9.4)
Requirement already satisfied: namex in /usr/local/lib/python3.12/dist-packages (from keras>=2.0.0->fer) (0.1.0)
Requirement already satisfied: h5py in /usr/local/lib/python3.12/dist-packages (from keras>=2.0.0->fer) (3.15.0)
Requirement already satisfied: optree in /usr/local/lib/python3.12/dist-packages (from keras>=2.0.0->fer) (0.17.0)
Requirement already satisfied: ml-dtypes in /usr/local/lib/python3.12/dist-packages (from keras>=2.0.0->fer) (0.5.3)
Requirement already satisfied: packaging in /usr/local/lib/python3.12/dist-packages (from keras>=2.0.0->fer) (25.0)
INFO: pip is looking at multiple versions of facenet-pytorch to determine which version is compatible with other requirements. This could take a while.
Collecting facenet-pytorch (from fer)
  Downloading facenet_pytorch-2.5.3-py3-none-any.whl.metadata (13 kB)
Requirement already satisfied: torchvision in /usr/local/lib/python3.12/dist-packages (from facenet-pytorch->fer) (0.23.0+cu126)
Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib->fer) (1.3.3)
Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.12/dist-packages (from matplotlib->fer) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib->fer) (4.60.1)
Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib->fer) (1.4.9)
Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib->fer) (3.2.5)
Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.12/dist-packages (from matplotlib->fer) (2.9.0.post0)
Requirement already satisfied: decorator<5.0,>=4.0.2 in /usr/local/lib/python3.12/dist-packages (from moviepy->fer) (4.4.2)
Requirement already satisfied: proglog<=1.0.0 in /usr/local/lib/python3.12/dist-packages (from moviepy->fer) (0.1.12)
Requirement already satisfied: imageio<3.0,>=2.5 in /usr/local/lib/python3.12/dist-packages (from moviepy->fer) (2.37.0)
Requirement already satisfied: imageio-ffmpeg>=0.2.0 in /usr/local/lib/python3.12/dist-packages (from moviepy->fer) (0.6.0)
Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests->fer) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests->fer) (3.11)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests->fer) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests->fer) (2025.10.5)
Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas->fer) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas->fer) (2025.2)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.7->matplotlib->fer) (1.17.0)
Requirement already satisfied: typing-extensions>=4.6.0 in /usr/local/lib/python3.12/dist-packages (from optree->keras>=2.0.0->fer) (4.15.0)
Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.12/dist-packages (from rich->keras>=2.0.0->fer) (4.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.12/dist-packages (from rich->keras>=2.0.0->fer) (2.19.2)
Requirement already satisfied: torch==2.8.0 in /usr/local/lib/python3.12/dist-packages (from torchvision->facenet-pytorch->fer) (2.8.0+cu126)
Requirement already satisfied: filelock in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (3.20.0)
Requirement already satisfied: setuptools in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (75.2.0)
Requirement already satisfied: sympy>=1.13.3 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (1.13.3)
Requirement already satisfied: networkx in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (3.5)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (3.1.6)
Requirement already satisfied: fsspec in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (2025.3.0)
Requirement already satisfied: nvidia-cuda-nvrtc-cu12==12.6.77 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (12.6.77)
Requirement already satisfied: nvidia-cuda-runtime-cu12==12.6.77 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (12.6.77)
Requirement already satisfied: nvidia-cuda-cupti-cu12==12.6.80 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (12.6.80)
Requirement already satisfied: nvidia-cudnn-cu12==9.10.2.21 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (9.10.2.21)
Requirement already satisfied: nvidia-cublas-cu12==12.6.4.1 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (12.6.4.1)
Requirement already satisfied: nvidia-cufft-cu12==11.3.0.4 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (11.3.0.4)
Requirement already satisfied: nvidia-curand-cu12==10.3.7.77 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (10.3.7.77)
Requirement already satisfied: nvidia-cusolver-cu12==11.7.1.2 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (11.7.1.2)
Requirement already satisfied: nvidia-cusparse-cu12==12.5.4.2 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (12.5.4.2)
Requirement already satisfied: nvidia-cusparselt-cu12==0.7.1 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (0.7.1)
Requirement already satisfied: nvidia-nccl-cu12==2.27.3 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (2.27.3)
Requirement already satisfied: nvidia-nvtx-cu12==12.6.77 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (12.6.77)
Requirement already satisfied: nvidia-nvjitlink-cu12==12.6.85 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (12.6.85)
Requirement already satisfied: nvidia-cufile-cu12==1.11.1.6 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (1.11.1.6)
Requirement already satisfied: triton==3.4.0 in /usr/local/lib/python3.12/dist-packages (from torch==2.8.0->torchvision->facenet-pytorch->fer) (3.4.0)
Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.12/dist-packages (from markdown-it-py>=2.2.0->rich->keras>=2.0.0->fer) (0.1.2)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.12/dist-packages (from sympy>=1.13.3->torch==2.8.0->torchvision->facenet-pytorch->fer) (1.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->torch==2.8.0->torchvision->facenet-pytorch->fer) (3.0.3)
Downloading fer-22.5.1-py3-none-any.whl (1.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.5/1.5 MB 17.8 MB/s eta 0:00:00
Downloading facenet_pytorch-2.5.3-py3-none-any.whl (1.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.9/1.9 MB 32.9 MB/s eta 0:00:00
Building wheels for collected packages: ffmpeg
  Building wheel for ffmpeg (setup.py) ... done
  Created wheel for ffmpeg: filename=ffmpeg-1.4-py3-none-any.whl size=6083 sha256=0415cf17c17bfb449b63905ab76957b37c5c2dd564fc64ce8b916eea99ac1f12
  Stored in directory: /root/.cache/pip/wheels/26/21/0c/c26e09dff860a9071683e279445262346e008a9a1d2142c4ad
Successfully built ffmpeg
Installing collected packages: ffmpeg, facenet-pytorch, fer
Successfully installed facenet-pytorch-2.5.3 fer-22.5.1 ffmpeg-1.4
/usr/local/lib/python3.12/dist-packages/moviepy/config_defaults.py:47: SyntaxWarning: invalid escape sequence '\P'
  IMAGEMAGICK_BINARY = r"C:\Program Files\ImageMagick-6.8.8-Q16\magick.exe"
/usr/local/lib/python3.12/dist-packages/moviepy/video/io/ffmpeg_reader.py:294: SyntaxWarning: invalid escape sequence '\d'
  lines_video = [l for l in lines if ' Video: ' in l and re.search('\d+x\d+', l)]
/usr/local/lib/python3.12/dist-packages/moviepy/video/io/ffmpeg_reader.py:367: SyntaxWarning: invalid escape sequence '\d'
  rotation_lines = [l for l in lines if 'rotate          :' in l and re.search('\d+$', l)]
/usr/local/lib/python3.12/dist-packages/moviepy/video/io/ffmpeg_reader.py:370: SyntaxWarning: invalid escape sequence '\d'
  match = re.search('\d+$', rotation_line)
WARNING:py.warnings:/usr/local/lib/python3.12/dist-packages/moviepy/video/io/sliders.py:61: SyntaxWarning: "is" with 'str' literal. Did you mean "=="?
  if event.key is 'enter':

xukai.jpg
xukai.jpg(image/jpeg) - 78484 bytes, last modified: 11/19/2023 - 100% done
Saving xukai.jpg to xukai.jpg
WARNING:py.warnings:/usr/local/lib/python3.12/dist-packages/keras/src/models/functional.py:241: UserWarning: The structure of `inputs` doesn't match the expected structure.
Expected: ['input_1']
Received: inputs=Tensor(shape=(1, 64, 64))
  warnings.warn(msg)


Predicted Expression: happy
All Emotions: {'angry': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happy': 1.0, 'sad': 0.0, 'surprise': 0.0, 'neutral': 0.0}
