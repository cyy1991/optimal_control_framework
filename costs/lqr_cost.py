from optimal_control_framework.costs import AbstractCost
import numpy as np

class LQRCost(AbstractCost):
  def __init__(self, N, Q, R, Qf, xd=None):
    """
    Assuming Q,R,Qf are vectors of appropriate length
    xd can be a single goal state or a matrix [N+1, n].
    If nothing provided then treated as zero
    vector
    """
    super(LQRCost, self).__init__(N)
    self.Q = Q
    self.R = R
    self.Qf = Qf
    n = self.Q.shape[0]
    if xd is None:
        self.xd = np.zeros((N+1, n))
    elif xs.shape[0] == N+1:
        self.xd = xd
    elif xs.shape[0] == n:
        self.xd = np.stack(xd, (N+1, 1))

  def stagewise_cost(self, i, x, u):
    xdiff =  x - self.xd[i]
    return np.dot(xdiff,self.Q*xdiff) + np.dot(u,self.R*u)

  def terminal_cost(self, xf):
    xdiff =  xf - self.xd[-1]
    return np.dot(xdiff,self.Qf*xdiff)
    
