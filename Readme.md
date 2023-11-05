# Lip-Sync AI using Wave2Lip

Effortlessly sync audio and video with our cutting-edge AI model (LOL), backed by the Face Restoration AI (GFPGAN) for exceptional visual quality. 
It is a lip-sync perfection! 🎤💫

## Input

Video - (https://openinapp.co/5cwva)

Audio - (https://openinapp.co/o9vuj)

## OUTPUT

Output Video - (https://drive.google.com/drive/folders/1cXaXb-rW8m8Fn8-_ZmwAdAz7BZ2ly0ZF?usp=sharing)


### How to run:

Google Collab :

		# Run the lip_syncing.ipynb file inside google collab!
		# Don;t forget to change runtime type to gpu

Local System :

Follow the steps:

1. Clone the Repository

Clone this GitHub repository to your local machine

2. Download Pre-trained Models

Download the necessary pre-trained models:

Face Detection Model :

wget 'https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth' -O './Lip-Sync-Repo/Wav2Lip/face_detection/detection/sfd/s3fd.pth'

Wave2Lip Model :

wget 'https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/download.aspx?share=EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA' -O './Lip-Sync-Repo/Wav2Lip/checkpoints/wav2lip_gan.pth'


3. install the requirement.txt   

4. Install ffmpeg

5. Install Nvidia cuda

6. Install pytorch

7. Run Lip_Sync.py


### References

[Wave2Lip](https://github.com/Rudrabha/Wav2Lip)

[GFPGAN](https://github.com/TencentARC/GFPGAN)

[Wave2Lip-GFPGAN](https://github.com/ajay-sainy/Wav2Lip-GFPGAN)

[Wave2Lip-ai](https://github.com/stokome/LipSync-wave2lip-ai)


