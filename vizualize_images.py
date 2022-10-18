import matplotlib.pyplot as plt

def visualize(data_gen,labels)
  '''Vizualize random images from dataset
    Params:
      data_gen : keras.preprocessing.image.DirectoryIterator object
      labels : numpy array of class names
    '''

  plt.figure(figsize=(10, 10))
  for images, labels in train_generator:
    for i in range(9):
      ax = plt.subplot(3, 3, i + 1)
      plt.imshow(images[i])
      plt.title(class_names[np.argmax(labels[i])])
      plt.axis("off")
    break
 
def visualize2(dataset,labels):
  '''VIsualize random images from dataset
   Params:
    dataset : BatchDataset object
    labels : numpy array of class names
    '''
  plt.figure(figsize=(10, 10))
  for images, labels in train_ds.take(1):
    for i in range(9):
      ax = plt.subplot(3, 3, i + 1)
      plt.imshow(images[i].numpy().astype("uint8"))
      plt.title(class_names[labels[i]])
      plt.axis("off")
