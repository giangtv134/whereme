from PIL import Image
import face_recognition
import os
import shutil

def find_person_in_images(person_image_path, images_folder_path, output_folder_path):
  """
  Finds and copies images containing the given person from the source folder to the output folder.

  Args:
    person_image_path: Path to the image of the person to be found.
    images_folder_path: Path to the folder containing images to search.
    output_folder_path: Path to the folder where matching images will be copied.

  Raises:
    FileNotFoundError: If the person image, source folder, or output folder does not exist.
  """

  if not os.path.exists(person_image_path):
    raise FileNotFoundError(f"Person image not found at {person_image_path}")

  if not os.path.exists(images_folder_path):
    raise FileNotFoundError(f"Images folder not found at {images_folder_path}")

  if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

  # Load the image of the person to be found
  person_image = face_recognition.load_image_file(person_image_path)
  person_face_encoding = face_recognition.face_encodings(person_image)[0]

  count = 0

  for filename in os.listdir(images_folder_path):
    print(f"🤔CHECKING {filename}...")
    image_path = os.path.join(images_folder_path, filename)
    try:
      image = face_recognition.load_image_file(image_path)
      face_locations = face_recognition.face_locations(image)
      face_encodings = face_recognition.face_encodings(image, face_locations)

      for face_encoding in face_encodings:
        # Compare faces
        match = face_recognition.compare_faces([person_face_encoding], face_encoding)
        if match[0]:
          count += 1
          print(f"✅FOUND in {filename}")
          shutil.copy2(image_path, output_folder_path)
          break  # No need to check other faces in the same image
      print("End. Found: ", count, " images")
    except IndexError:
      # No faces found in the image
      pass

if __name__ == "__main__":
  person_image_path = os.environ.get("ME")
  images_folder_path = os.environ.get("IN")
  output_folder_path = os.environ.get("OUT")

  find_person_in_images(person_image_path, images_folder_path, output_folder_path)
