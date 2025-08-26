def get_size(w,h,d): #tres argumentos que calculan el area y volumen de un cubo.
    area = 2 * ((w *h) + (w * d) + (h * d))
    volumen = w * h * d
    return [area, volumen]