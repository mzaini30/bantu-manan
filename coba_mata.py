import cv2
import time
import winsound

deteksi_mata = cv2.CascadeClassifier('haarcascade_eye.xml')
deteksi_wajah = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


kamera = cv2.VideoCapture(1)
hitung = 0
buka = 0
kedip = 0
dakhir = 0
dawal = 0
jumlahan = 0

while(True): 
    ret, frame = kamera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    wajah = deteksi_wajah.detectMultiScale(gray,scaleFactor = 1.1, minNeighbors=1, minSize=(10,10))
    for (x,y,w,h) in wajah:
      roi_gray = gray[y:y+h, x:x+w]
      roi_color = frame[y:y+h, x:x+w]
      mata = deteksi_mata.detectMultiScale(roi_gray)
      start_time = time.time()
      if len(mata) == 0:
          hitung = hitung + 1
          print ("Durasi Mata Tertutup ==========> ", hitung)
          dawal = time.time() - start_time
          print("--- %s seconds MATA TERTUTUP---" % (dawal))
          dakhir = dakhir + dawal 
          print("--- %s D AKHIR---" % (dakhir))
          if dakhir >= 0.8 or hitung >=3:
              print ("Ngantuk")
              winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
      else:
          dakhir = 0
          print ("Mata Terbuka")

      if hitung == 1:
           kedip = kedip + 1
           print('jumlah kedipan ==========================>' ,kedip)
           print("\n")
      
      
      for (ex,ey,ew,eh) in mata:
             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      cv2.destroyAllWindows()
      break
    
        
            
