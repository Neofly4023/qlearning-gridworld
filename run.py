from environment import Env
from QLearning import QLearning


if __name__=="__main__":
    env = Env()
    QL = QLearning(list(range(env.n_actions)))

    for episode in range(30):
        state = env.reset()
        while True:
            env.render()

            # take action and proceed one step in the environment
            action = QL.get_action(str(state))
            next_state, reward, done = env.step(action)

            #env.print_value_all(QL.q_table)

            # with sample <s,a,r,s'>, agent learns new q function
            # Uncomment this
            QL.learn(str(state), action, reward, str(next_state))
            print ("<state:{0} , action:{1} , reward:{2} , next_state:{3}>".format(str(state), str(action), str(reward), str(next_state)) )

            env.print_value_all(QL.q_table)

            state = next_state
            # Uncomment this
            #env.print_value_all(QL.q_table)

            # if episode ends, then break
            if done:
                break
