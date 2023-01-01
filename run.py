import cv2
list_of_names = []

def cleanup_data():
    with open("names.txt") as file:
        for line in file:
            list_of_names.append(line.strip())
def generate_certificate():
    for index, name in enumerate(list_of_names):
        template = cv2.imread("Certificate-Template.jpg")
        cv2.putText(template, name, (487,853), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 5, (202, 181, 60), 5, cv2.LINE_AA)
        cv2.imwrite(f'Generated-Certificates/{name}.jpg', template)
        print(f'Processing {index + 1} / {len(list_of_names)}')

cleanup_data()
generate_certificate()
