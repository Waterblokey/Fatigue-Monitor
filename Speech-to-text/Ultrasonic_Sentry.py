import serial
import cv2

# Setup serial connection (adjust COM port as needed)
arduino = serial.Serial('COM4', 9600)
trigger_distance = 20  # Trigger distance in cm

# Setup OpenCV to record video
cap = cv2.VideoCapture(0)  # Start video capture on the default camera


#records video
def record_video():
    started = False #flag used to check if video started recording
    #formats video and saves
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
    #where the recording happens
    while (True):
        ret, frame = cap.read() #grabs and reads frames
        #if it fails 
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow('frame', frame) #show the frames

        key = cv2.waitKey(1) #initializes key to read keyboard input
        #uses flag to start recording
        if(not started):
            print("Recording started...")
            started = True
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Failed to grab frame")
                    break
                out.write(frame)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) == ord('q'):  # Stop recording when 'q' is pressed
                    print("Recording stopped.")
                    break
            if cv2.waitKey(1) == ord('q'):  # Stop recording when 'q' is pressed
                break
    #closes camera window      
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    

#Main loop to read from Arduino and check distance which triggers recording
try:
    while True:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode().strip()
            if line.startswith('Distance:'):
                distance_str = line.split(':')[1].strip()  # Extract the numeric part of the line after the colon
                try:
                    distance = float(distance_str)  # Convert the extracted string to float
                    print(f"Distance: {distance} cm")
                    if distance < trigger_distance: #if distance is close, then call function to record data
                        print("Object too close! Starting video recording...")
                        record_video()
                        

                except ValueError:
                    print("Error: Invalid distance value")
except KeyboardInterrupt:
    print("Program interrupted by user")
finally:
    arduino.close()