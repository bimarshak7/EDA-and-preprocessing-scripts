def compare_historys(previous_history, new_history, initial_epochs=5):
    """
    Compares two model history objects (model trained using checkpoints).
    Parameters:
    previous_history: history object of previous model
    new_history : history object of new_model
    initial_epoch : number of epoch the model was trained previously
    """
    # Get original history measurements
    acc = previous_history.history["accuracy"]
    loss = previous_history.history["loss"]

    print(len(acc))

    val_acc = previous_history.history["val_accuracy"]
    val_loss = previous_history.history["val_loss"]

    # Combine original history with new history
    total_acc = acc + new_history.history["accuracy"]
    total_loss = loss + new_history.history["loss"]

    total_val_acc = val_acc + new_history.history["val_accuracy"]
    total_val_loss = val_loss + new_history.history["val_loss"]

    print(len(total_acc))
    print(total_acc)

    # Make plots
    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    plt.plot(total_acc, label='Training Accuracy')
    plt.plot(total_val_acc, label='Validation Accuracy')
    plt.plot([initial_epochs-1, initial_epochs-1],
    plt.ylim(), label='Start Fine Tuning') # reshift plot around epochs
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy -Previous model')

    plt.subplot(2, 1, 2)
    plt.plot(total_loss, label='Training Loss')
    plt.plot(total_val_loss, label='Validation Loss')
    plt.plot([initial_epochs-1, initial_epochs-1],
              plt.ylim(), label='Start Fine Tuning') # reshift plot around epochs
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss- New Model')
    plt.xlabel('epoch')
    plt.show()
