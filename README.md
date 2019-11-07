# 107 Video Processing

視訊處理
教授: 黃世育

by [roy4801](https://github.com/roy4801)


## Review
> 406262515 資工二乙 鍾秉桓
> 406262163 資工二乙 黃品翰

## 上學期

上學期的pygame專案，我們這組做2D的射擊遊戲，但就跟許多專案一樣，開頭想的feature一大堆，但最後真正實作的功能跟當初想的可能不一樣，這次我們從蠻底層開始刻，算是生出了一個簡單的framework。我們的開發分成兩階段:

### [RHframework](https://github.com/roy4801/RHframework)

* 特點
	* 使用pygame，imgui
	* 渲染改成OpenGL(但是是2.0的)，但還是比CPU快很多了
	* 簡易UI, sound, image等封裝，方便開發

撰寫這個framework花了我們2/3的時間，大部分時間都在想介面(interface)該怎麼寫，算是多了一個開發library的經驗，(但其實跟production的library還差得很遠)

### [rifleman](https://github.com/william31212/Pygame)

* 使用RHframework
* 使用Tiled作為地圖編輯器

原本是想做2D的roguelike的ARPG，但是我們錯估了時間，導致在開發遊戲時程不足，所以完成度並沒有當初預想的那樣。

## 下學期

這個專案由於我還有其他課(Web)的專案時間影響，所以並沒有花很多心思在上頭。