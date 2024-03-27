class StreetViewImage:
    
    def __init__(self, pic_json, location, bearing, date, pano_id):
        self.folder_dir = "../images"
        self.pic_json = pic_json
        self.location = location
        self.bearing = bearing
        self.date = date
        self.pano_id = pano_id
    
    def get_prefix(self):
        return '{}_{}_{}_{}.jpg'.format(self.location, str(int(self.bearing)), self.date, self.pano_id)
        
    def save_to_file(self, folder_dir):
        prefix = StreetViewImage.get_prefix(self)
        file_path = os.path.join(self.folder_dir, prefix)
        with open(file_path, 'wb') as f:
            f.write(self.pic_json.content)
        return file_path