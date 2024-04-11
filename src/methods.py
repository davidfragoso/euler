#Para hacer calculitos en euler estandar
def euler(f, x0, y0, h, n):
    xs = [x0]
    ys = [y0]
    x = x0
    y = y0
    for _ in range(n):
        y += h * f(x, y)
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys

#Para hacer calculitos en euler estandar mejorado
def improved_euler(f, x0, y0, h, n):
    xs = [x0]
    ys = [y0]
    x = x0
    y = y0
    for _ in range(n):
        y_pred = y + h * f(x, y)
        y += h * (f(x, y) + f(x + h, y_pred)) / 2
        x += h
        xs.append(x)
        ys.append(y)
    return xs, ys
