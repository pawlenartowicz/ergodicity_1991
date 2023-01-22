import sys
sys.path.insert(0, r'D:\GitHub\ergodicity_1991\detection_gan')
from training_loop import training_loop
from generator_discriminator import Generator, Discriminator
from transformers import get_linear_schedule_with_warmup
import wandb
import torch

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

layer_sizes = [100, 500, 1000, 2000]

generator = Generator(layer_sizes, 4000)

layer_sizes = [2000, 1000, 500, 100]
discriminator = Discriminator(layer_sizes, 1)

generator = generator.to(device)
discriminator = discriminator.to(device)

optimizer_generator = torch.optim.AdamW(generator.parameters(),
                    lr=5e-4,
                    eps=1e-8,  # Epsilon
                    weight_decay=0.3,
                    amsgrad=True,
                    betas = (0.9, 0.999))

optimizer_discriminator = torch.optim.AdamW(discriminator.parameters(),
                    lr=5e-4,
                    eps=1e-8,  # Epsilon
                    weight_decay=0.3,
                    amsgrad=True,
                    betas = (0.9, 0.999))

scheduler = get_linear_schedule_with_warmup(optimizer,
                                            num_warmup_steps=500,
                                            num_training_steps= len(train_dataloader) * epochs)

criterion = torch.nn.BCELoss()
critic_range = 3
save_dir = r'D:\GitHub\ergodicity_1991\detection_gan\models\test_1'
epochs = 10
batch_size = 1000

wandb.init(project="detection_gan", entity="hubertp")
wandb.watch(generator, log_freq=5)
wandb.watch(discriminator, log_freq=5)

training_loop(generator, discriminator, epochs, batch_size, device, save_dir,
              optimizer_generator, optimizer_discriminator, criterion,
              scheduler, critic_range)


