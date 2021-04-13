# Article
Cui, Y. R., Liu, Q., Gao, C. Y., & Su, Z. (2018). FashionGAN: Display your fashion design using Conditional Generative Adversarial Nets. Computer Graphics Forum, 37(7), 109–119. https://doi.org/10.1111/cgf.13552

# Aim

it can directly show the design effect of the garment

# Background

## Vistual garment display

### 3D virtual garment display methods

Plenty of display methods have been proposed to preview virtual garments in recent years. Most of them focus on displaying the 3D virtual garment.

These systems require significant time and domain-specific user knowledge to create patterns that achieve adesired 3D garment.

These systems create garment models which are frequently simple, non-physical and hence unrealizable.

### 2D virtual garment display
avoids the demand for domainspecific user knowledge and time-consuming of the traditional garment modeling.

## image to image GAN

GAN + conditionals to constrain the generator = Conditional GAN(cGAN)

### BicycleGAN

takes advantage of cVAE-GAN and cLR-GAN

two issues:

1. the ground truth is always unavailable, especially in fashion design fields.(Shape information conveyed by two different inputs)

2. texture details in fabric pattern cannot be restored with only L1 loss


# Methods
the shape of the final generated image is constrained by fashion sketch/contour image, and the color together with the material is constrained by the fabric pattern. Then we add an extra local loss module to control the generator synthesizing texture.

loss function: 

LNetA(G;D;E)=LGAN(G;D;E)+limLim 1 (G;E)+lKLLKL(E)+Lt

# Results

Human preference: compare with other GANs

Inception score(A higher inception score means high-quality and diverse): need to to add a content encoder to the diversity of results.

# Comments

it cannot map an irregular on: need to construct a new local loss module describing the irregular texture.

extend our model to more general image translation tasks, like image colorization and style transfer.

# Why
* understand the background of the subject
* experimental design
* writing imitation
