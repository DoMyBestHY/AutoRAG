import os
import azure.cognitiveservices.speech as speechsdk

def readAzure(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            azure_key  = lines[0].strip()
            azure_region = lines[1].strip()
            return azure_key, azure_region
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
    
# azure_key, azure_region = readAzure('C:/Users/emati/OneDrive/바탕 화면/한이음/STT/Azure.txt')

os.environ['SPEECH_KEY'] = '47833291818e43dd845241deba83d354'
os.environ['SPEECH_REGION'] = 'koreacentral'  # 예: 'westus'

# export SPEECH_KEY="YourAzureSpeechKey"
# export SPEECH_REGION="eastus"


def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))

    speech_config.speech_recognition_language="ko-KR"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

recognize_from_microphone()
