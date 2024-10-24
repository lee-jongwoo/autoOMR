# TF 모델을 학습하고 가중치를 저장하는 스크립트.
# 프로그램 실행 시에는 작동하지 않고, 최초 1회 실행하여 가중치 저장용으로만 사용한다.

from tensorflow.keras import datasets, layers, models
import os

# 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# CNN 모델 구성
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 가중치를 저장할 디렉토리 생성
save_dir = 'weights'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 가중치를 저장할 파일 경로
weights_path = os.path.join(save_dir, 'mnist_cnn.weights.h5')

# 모델 학습
model.fit(train_images, train_labels, epochs=5, validation_data=(test_images, test_labels))

# 가중치 저장
model.save_weights(weights_path)
print(f"학습된 가중치가 저장되었습니다: {weights_path}")

# 모델 평가
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f"테스트 정확도: {test_acc}")