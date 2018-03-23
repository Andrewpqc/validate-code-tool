# ValidateCodeTool
A simple library  to help you to generate authentication code. It's flexible and convenient.

## Install
``` bash
$ pip install validateCodeTool
```

## Usage
``` python
import validateCodeTool
img, code = validateCodeTool.create_validate_code()
print("the code is:", code)
with open("check_code.gif", "wb") as f:
    img.save(f)
```

## Custom picture
There is only one function in this package, that is **create_validate_code()**. This function can work normally without any parameter. At the same time, you can pass some parameters to customize the function's behavior. The following table shows the parameters that you can customize.

| parameters | behavior | default value | available value |
| :---------: | :----------: | :---------: | :------------: |
|     size    | (width,hight) | (120,30)   |      custom   |
|     chars   |  chars allowed | a-h,j-k,m-n,p-y,A-H,J-K,M-N,P-Y,3-9 | custom |
| img_type    |  image type   | GIF       | GIF,JPEG,TIFF,PNG  |
|  mode       |  image mode   | RGB       | RGB      |
|   bg_color  | background color | (255,255, 200) | (R,G,B) ,0<=R,G,B<=255  |
| fg_color    | foreground color | ((0, 125, 255)) | (R,G,B) ,0<=R,G,B<=255 |
| font_size   |  font size       |   18px         |  >=0  |
| font_type   | font type        | ae_AlArabiya.ttf    | custom |
|  length     | the number of chars in image  |  4     |  >=1   |
| draw_lines  |  Whether or not to draw interference lines  | True | True,False |
| n_lines     | the number of interference lines |   (1,2)     |  custom   |
| draw_points | Whether or not to draw interference points | True | True,False  |
| transform   | Whether or not to add distortion  |　False　| True,False |
| withfilter  |Whether or not to add filter      |  False | True,False |
| point_chance | Frequency of interference point |  2      | 0<=x<=100 |          |

## Example
``` bash
$ git clone https://github.com/Andrewpqc/authentication_code_generator.git && cd authentication_code_generator/example_app && pip install -r requirements.txt && python example_app.py 
```
Then you can go to your browser at "http://127.0.0.1:5000/example-app/" to see the example!