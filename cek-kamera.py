import cv2
import mediapipe as mp # type: ignore
import math
import os
import pygame
from typing import Any

pygame.mixer.init()

# Cek gerakanya berdasarkan pose pergelangan tangan dan siku
mp_pose: Any = mp.solutions.pose # type: ignore
pose: Any = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) # type: ignore

cap = cv2.VideoCapture(0)
meme_video_path = "meme.mp4" # ini bisa di ubah dengan video lain ya..
meme_audio_path = "meme_audio.mp3" # abistu buat versi suaranya juga..
motion_detected = False

hold_counter = 0 
REQUIRED_HOLD_FRAMES = 15

print("Sistem Aktif! Pastiin bahu kamu masuk frame agar pendeteksi stabil.")

while cap.isOpened():
    success, image = cap.read()
    if not success: break

    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb) # type: ignore

    status_text = "Nyari Pose..."

    if results.pose_landmarks:  # type: ignore
        # Buat nentuin titik pergelangan tangan kiri dan kanan
        lw = results.pose_landmarks.landmark[15]  # type: ignore
        rw = results.pose_landmarks.landmark[16]  # type: ignore

        distance = math.sqrt((lw.x - rw.x)**2 + (lw.y - rw.y)**2)  # type: ignore

        # Logika: Buat rapetin tangan
        if distance < 0.20: 
            hold_counter += 1
            status_text = f"MEMOHON TERDETEKSI WOI! TAHAN GERAKANYA: {hold_counter}"
            
            if hold_counter >= REQUIRED_HOLD_FRAMES:
                motion_detected = True
                break
        else:
            hold_counter = 0
            status_text = f"Jarak: {distance:.2f} (Rapatin Tangan)"


    cv2.putText(image, status_text, (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    cv2.imshow('Monitoring', image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()

if motion_detected:
    if os.path.exists(meme_audio_path):
        pygame.mixer.music.load(meme_audio_path)
        pygame.mixer.music.play()

    meme_cap = cv2.VideoCapture(meme_video_path)
    while meme_cap.isOpened():
        ret, frame = meme_cap.read()
        if not ret: break 
        cv2.imshow('MEME KEBACA!', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'): break
    meme_cap.release()
    pygame.mixer.music.stop()
    cv2.destroyAllWindows()