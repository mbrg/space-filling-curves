import numpy as np
from matplotlib import animation, rc, pyplot as plt
from curves import Curve_2D


def animate_curve(curve, curve_intensity=255, msecs_per_frame=6):
    """
    Create an animation of a space filling curve
    :param curve: Curve_2D
    :param curve_intensity: pixel intensity to be used for curve animation
    :param msecs_per_frame: delay between frames in milliseconds
    :return: an animation object
    """

    assert isinstance(curve, Curve_2D), "curve must be of type Curve_2D"


    fig = plt.figure()
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
    plt.axis('off')

    # start with a white image
    blank_img = np.multiply(np.ones((curve.size, curve.size)), curve_intensity).astype(np.int)
    blank_img[0] = 0  # hack to prevent plt from presenting a black figure
    im = plt.imshow(blank_img, 'gray', animated=True)
    plt.close(fig)
    cur_frame, cur_coor = blank_img, None

    def updatefig(*args):
        #global cur_coor, cur_frame
        try:
            cur_coor = curve.next_coor()
            cur_frame[cur_coor[0], cur_coor[1]] = 0
        except StopIteration:
            pass
        im.set_array(cur_frame)
        return im,

    # record video and save/inline
    ani = animation.FuncAnimation(fig, updatefig, frames=pow(curve.size, 2), interval=msecs_per_frame, blit=True)
    rc('animation', html='html5')

    return ani