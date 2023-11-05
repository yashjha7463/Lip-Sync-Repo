# Lip-Sync AI using Wave2Lip

Effortlessly sync audio and video with our cutting-edge AI model (LOL), backed by the Face Restoration AI (GFPGAN) for exceptional visual quality. 
It is a lip-sync perfection! 🎤💫

## Input

Video - (https://openinapp.co/5cwva)

Audio - (https://openinapp.co/o9vuj)

## Results

Generated Lip Synced Video - [View on GitHub](https://github.com/stokome/LipSync-wave2lip-ai/assets/87638990/75dde50e-ca58-4d1b-9153-0bfd3045f981)


### Use of Image Restoration AI GFPGAN_ 
Video quality was improved when I replaced wave2lip.pth weigths with wave2lip_gan weights. Further improvement was done using GFPGAN. GFPGAN is an image restoration AI. To use it on our inference we first divided the output images into frames, improved quality of each frame independently and then combined the frames in 25fps and audio.

### How to run:

Google Collab :
		# Run the lip_syncing.ipynb file inside google collab!

Local System :

Follow the steps:

1. Clone the Repository

Clone this GitHub repository to your local machine

2. Download Pre-trained Models

Download the necessary pre-trained models:

Face Detection Model :

wget 'https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth' -O './LipSync-wave2lip-project/Wav2Lip/face_detection/detection/sfd/s3fd.pth'

Wave2Lip Model :

wget 'https://iiitaphyd-my.sharepoint.com/personal/radrabha_m_research_iiit_ac_in/_layouts/15/download.aspx?share=EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA' -O './LipSync-wave2lip-ai/Wav2Lip/checkpoints/wav2lip_gan.pth'

3. Install ffmpeg

4. Run Lip_Sync.py


### References

[Wave2Lip](https://github.com/Rudrabha/Wav2Lip)

[GFPGAN](https://github.com/TencentARC/GFPGAN)

[Wave2Lip-GFPGAN](https://github.com/ajay-sainy/Wav2Lip-GFPGAN)

[Wave2Lip-ai](https://github.com/stokome/LipSync-wave2lip-ai)


