from skills.error_handling import log_error

def coordinate_agents(agent_functions):
    results = {}
    for agent_name, agent_function in agent_functions.items():
        try:
            results[agent_name] = agent_function()
        except Exception as e:
            log_error(f"Agent {agent_name} failed: {str(e)}")
    return results
