import cv2
import numpy as np
from numpy import uint8

#入力されたファイル名をグレースケールで読み込む
imname=input("Please input File Path : ")
im=cv2.imread(imname,cv2.IMREAD_GRAYSCALE)
height,width=im.shape
stat=np.zeros((height,width))
single=np.zeros((height,width))

#フーリエ変換をし、パワースペクトラムを計算
fx=np.fft.fft2(im)
fx2=np.fft.fftshift(fx)
fft=20*np.log(np.abs(fx2))
M_fft=int(np.max(fft))
m_fft=int(np.min(fft))

#マウスイベント処理
def mouse_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        single[:,:]=0
        stat[y,x]=1.0
        single[y,x]=1.0
        
    if event==cv2.EVENT_RBUTTONDOWN:
        single[:,:]=0
        stat[y-5:y+5,x-5:x+5]=1.0
        single[y-5:y+5,x-5:x+5]=1.0
        
    if event==cv2.EVENT_MOUSEMOVE:
            if flags==cv2.EVENT_FLAG_LBUTTON:
                single[:,:]=0
                stat[y,x]=1.0
                single[y,x]=1.0
            if flags==cv2.EVENT_FLAG_RBUTTON:
                single[:,:]=0
                stat[y-5:y+5,x-5:x+5]=1.0
                single[y-5:y+5,x-5:x+5]=1.0

while True:
    #今までマウスで選択した部分の逆フーリエ変換
    b_fx=np.fft.fftshift(fx2*stat)
    b_im=np.fft.ifft2(b_fx)
    B_im=np.abs(b_im)
    B_max=np.max(B_im)
    B_min=np.min(B_im)
    
    #現在マウスで選択した部分だけの逆フーリエ変換
    s_fx=np.fft.fftshift(fx2*single)
    s_im=np.fft.ifft2(s_fx)
    S_im=np.abs(s_im)
    S_max=np.max(S_im)
    S_min=np.min(S_im)
    
    #画像の表示(それぞれ正規化してから表示)
    cv2.imshow("G_Original",im)
    cv2.imshow("FFT",((fft-m_fft)/(M_fft-m_fft)*255).astype(uint8))
    cv2.imshow("B_Image",((B_im-B_min)/(B_max-B_min)*255).astype(uint8))
    cv2.imshow("stat",stat)
    cv2.imshow("Single",((S_im-S_min)/(S_max-S_min)*255).astype(uint8))
    #マウスイベントを呼び出す
    cv2.setMouseCallback("stat",mouse_event)
    cv2.setMouseCallback("FFT",mouse_event)
    
    #[Esc]キーを押すと終了
    k=cv2.waitKey(1)
    if k==27:
        break

cv2.destroyAllWindows()        