import cv2

class Detector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.cameraMode = 1
        
    
    def detect_face(self):
        self.camera = cv2.VideoCapture(self.cameraMode)
        counter = 0
        while True:
            if counter > 5:
                self.camera.release()
                return (False,0)
            ret, frame = self.camera.read()
            if not ret:
                print("Kamera açılamadı.")
                self.camera.release()
                return False
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            
            if len(faces) > 0:
                print("Yüz bulundu!")
                self.camera.release()
                return (True,len(faces))
            else:
                counter+=1
                print("Yüz bulunamadı.")

        


