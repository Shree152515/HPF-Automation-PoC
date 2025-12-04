import os, shutil

incoming_folder = "incoming_docs"
archive_folder = "archive"
files = os.listdir(incoming_folder)

for fname in files:
    if fname.lower().endswith(('.pdf','.docx')):
        try:
            parts = fname.split('_')
            project, date, doc_type = parts[0], parts[1], parts[2].split('.')[0]
            dest_folder = os.path.join(archive_folder, project, date)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(os.path.join(incoming_folder,fname), os.path.join(dest_folder,fname))
            print(f"Moved {fname} -> {dest_folder}")
        except Exception as e:
            print(f"Error processing {fname}: {e}")

print("Document archiving completed!")