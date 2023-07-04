class ImageDataset(Dataset):
  """
    Create custom dataset object in pytorch. It will load images from a directory(without class/labels."
  """
  def __init__(self,dir,transform=None):
    self.img_dir = dir
    self.transform = transform
    self.images = os.listdir(self.img_dir)
  
  def __len__(self):
    return len(self.images)
  
  def __getitem__(self, idx):
    img_path = os.path.join(self.img_dir,self.images[idx])
    image = read_image(img_path)
    if self.transform:
      image = self.transform(image)
    return image

  def see_random(self,n,c):
    """
      Vizualize random images from custom dataset
      n: number of rows to show
      c: nubmer of columns per row
    """
    
    figure = plt.figure(figsize=(8, 8))
    idxs = torch.randint(1,len(self.images),(n*c,))
    for i in range(1,len(idxs)+1):
      figure.add_subplot(n, c, i)
      # print("Path",os.path.join(self.img_dir,self.images[idxs[i-1]]))
      image = read_image(os.path.join(self.img_dir,self.images[idxs[i-1]]))
      plt.imshow(image.squeeze().permute(1,2,0))
    plt.show()
