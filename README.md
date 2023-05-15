# ControlCollection
Collect and apply interesting control methods!!

### Reinforcement Learning Output Feedback NN Control Using Deterministic Learning Technique
[Paper](https://github.com/wwsyan/ControlCollection/blob/main/AC_RBF_feedback_control/binxu2014.pdf), 
[Repro](https://github.com/wwsyan/ControlCollection/tree/main/AC_RBF_feedback_control).
This work applies the common structure of Actor Critic network in Reinforcement Learning to feedback control, 
which to some extent satisfies the requirements of optimal control and adaptive control.

Run [run_0.py](https://github.com/wwsyan/ControlCollection/blob/main/AC_RBF_feedback_control/run_0.py) to get dynamics while u = y_d.

Run [run_1.py](https://github.com/wwsyan/ControlCollection/blob/main/AC_RBF_feedback_control/run_1.py) to get dynamics while u = actor output.
<img src="AC_RBF_feedback_control/img/actor_input.png" width="100%" height="100%">

