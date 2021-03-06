###########################
# 라이브러리 사용
import tensorflow as tf
import pandas as pd
 
###########################

# 데이터를 준비하고
(독립, 종속), _ = tf.keras.datasets.mnist.load_data()
# 컨벌루션 레이어는 shape가 꼭 3차원이야 한다. 따라서 3차원 형태로 바꿔줌.
독립 = 독립.reshape(60000, 28, 28, 1)
종속 = pd.get_dummies(종속)
print(독립.shape, 종속.shape)
 
# ###########################
# 모델을 만들고
X = tf.keras.layers.Input(shape=[28, 28, 1])
# 5*5 사이즈인 filter 3개를 사용
H = tf.keras.layers.Conv2D(3, kernel_size=5, activation='swish')(X)
# 5*5 사이즈인 filter 6개를 사용
H = tf.keras.layers.Conv2D(6, kernel_size=5, activation='swish')(H)
# 이미지 여러장인 데이터 결과물을 얻었음. 한줄로 펴서 표형태로 바꿔준다.
H = tf.keras.layers.Flatten()(H)
# dense layer
H = tf.keras.layers.Dense(84, activation='swish')(H)
# 10개 분류 만들기
Y = tf.keras.layers.Dense(10, activation='softmax')(H)
model = tf.keras.models.Model(X, Y)
model.compile(loss='categorical_crossentropy', metrics='accuracy')
 
# ###########################
# # 모델을 학습하고
# model.fit(독립, 종속, epochs=10)
 
# ###########################
# 모델을 이용합니다. 
pred = model.predict(독립[0:5])
pd.DataFrame(pred).round(2)
 
# 정답 확인
종속[0:5]
 
# 모델 확인
model.summary()