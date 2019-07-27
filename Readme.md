# PyFFT
任意の画像をグレースケールで読み込み、フーリエ変換後のパワースペクトラム・マウスで選択した部分のフーリエ逆変換をリアルタイムで表示するコードである

## 実行例

## 使い方
1. 最初に目的の画像ファイルのパスを入力する
2. ウインドウが５つ表示される
    - G_Original：グレースケールで読み込んだ画像の表示
    - FFT：フーリエ変換後のパワースペクトラムの表示
    - B_Image：statまたはFFTで、今までマウスで選択した領域をフーリエ逆変換したものを表示
    - stat：マウスで今まで選択した領域を視覚化して表示（選択したところは白くなる）
    - Single：現在マウスで選択している部分だけをフーリエ逆変換し、表示
3. FFTまたはstatウインドウから、マウスでフーリエ逆変換したい部分を選択する
    - 左クリック：１マス分選択
    - 右クリック：選択した部分を中心に（10,10）マス分選択
4. [Esc]キーを押すと終了する

## 依存ライブラリ
- opencv-python -_4.1.0_
- numpy -_1.16.2_

## 参考資料
- フーリエ変換について
    - numpyとopenCVを使った画像のフーリエ変換と逆変換-Python in the box  
    http://www.hello-python.com/2018/02/16/numpyとopencvを使った画像のフーリエ変換と逆変換/
- Pythonのマウスイベントについて
    - PythonとOpenCVで画像処理④【マウスイベント】 - 無能プログラマーのお勉強おメモ  
    http://rasp.hateblo.jp/entry/2016/01/24/204539
- 画像の正規化について
    - Pythonで正規化・標準化（リスト、NumPy配列、pandas.DataFrame）  
    https://note.nkmk.me/python-list-ndarray-dataframe-normalize-standardize/
