# Stress Test 001 — computed analysis

- total records: 168
- accepted: 142
- rejected: 26

## Rejection reasons
| value | count | % |
| --- | ---: | ---: |
| weak_total | 7 | 26.9 |
| duplicate_signature | 7 | 26.9 |
| physics_only_comedy | 5 | 19.2 |
| prop_swap | 4 | 15.4 |
| generic_no_hook | 2 | 7.7 |
| power_autosolve | 1 | 3.8 |
| unsafe_or_severe | 1 | 3.8 |
| competence_hierarchy | 1 | 3.8 |
| hidden_ensemble | 1 | 3.8 |
| dialogue_dependent_unfixable | 1 | 3.8 |
| too_abstract_for_core | 1 | 3.8 |

## Accepted: story family coverage
| value | count | % |
| --- | ---: | ---: |
| building | 5 | 3.5 |
| caring | 5 | 3.5 |
| celebration | 3 | 2.1 |
| choice_conflict | 5 | 3.5 |
| cleanup | 4 | 2.8 |
| collecting | 4 | 2.8 |
| competition | 5 | 3.5 |
| cooperation | 5 | 3.5 |
| embarrassment | 3 | 2.1 |
| environmental_change | 5 | 3.5 |
| exploration | 4 | 2.8 |
| fear_courage | 4 | 2.8 |
| finding_losing | 5 | 3.5 |
| helping | 5 | 3.5 |
| hiding_revealing | 4 | 2.8 |
| imitation | 6 | 4.2 |
| independent_goals | 3 | 2.1 |
| jealousy | 3 | 2.1 |
| misunderstanding | 6 | 4.2 |
| observation | 4 | 2.8 |
| patience | 4 | 2.8 |
| performance | 4 | 2.8 |
| preparing | 4 | 2.8 |
| repair | 4 | 2.8 |
| responsibility | 3 | 2.1 |
| routine_disruption | 5 | 3.5 |
| searching | 4 | 2.8 |
| sharing | 6 | 4.2 |
| simple_science | 4 | 2.8 |
| social_expectation | 4 | 2.8 |
| surprise | 4 | 2.8 |
| transporting | 4 | 2.8 |
| waiting | 4 | 2.8 |

Families with zero accepted premises: none

## Accepted: causal mechanisms
| value | count | % |
| --- | ---: | ---: |
| accident_plain | 7 | 4.9 |
| care_overreach | 9 | 6.3 |
| communication_gap | 4 | 2.8 |
| competitive_escalation | 4 | 2.8 |
| curiosity_experiment | 12 | 8.5 |
| divided_attention | 4 | 2.8 |
| feelings_leak | 10 | 7.0 |
| generosity_dilemma | 4 | 2.8 |
| imitation_mismatch | 4 | 2.8 |
| lost_hold | 4 | 2.8 |
| misread_signal | 13 | 9.2 |
| nature_course | 25 | 17.6 |
| order_vs_mess | 2 | 1.4 |
| other | 3 | 2.1 |
| over_preparation | 3 | 2.1 |
| promise_deadline | 6 | 4.2 |
| resource_split | 4 | 2.8 |
| rigid_plan_vs_reality | 5 | 3.5 |
| role_reversal | 3 | 2.1 |
| routine_break | 2 | 1.4 |
| stage_fright_visibility | 4 | 2.8 |
| suppression_backfire | 7 | 4.9 |
| weather_obstacle | 0 | 0.0 |
| weather_overshoot | 0 | 0.0 |
| weather_reveal | 3 | 2.1 |

## Accepted: distinct mechanism signatures
- distinct full signatures: 125 of 142 accepted
- distinct causal mechanisms used: 23 of 25 defined
- signatures shared by 2+ premises (near-dup candidates): 14

| signature | count | ids |
| --- | ---: | --- |
| shared|curiosity_experiment|plan|understanding | 4 | PN-3003, PN-3018, PN-3020, PN-3021 |
| nimbus|nature_course|feelings|acceptance | 3 | PN-2030, PN-3012, PN-4005 |
| nimbus|misread_signal|feelings|understanding | 2 | PN-1008, PN-4017 |
| shared|nature_course|plan|reframe | 2 | PN-1020, PN-2025 |
| shared|curiosity_experiment|plan|reframe | 2 | PN-2002, PN-3001 |
| third_force|nature_course|duty|joint_repair | 2 | PN-2003, PN-3026 |
| nimbus|care_overreach|duty|understanding | 2 | PN-2007, PN-4019 |
| shared|nature_course|duty|acceptance | 2 | PN-2008, PN-4004 |
| pip|nature_course|plan|reframe | 2 | PN-2010, PN-3013 |
| nimbus|care_overreach|plan|understanding | 2 | PN-2014, PN-3019 |
| shared|nature_course|duty|joint_repair | 2 | PN-2024, PN-4021 |
| nimbus|care_overreach|relationship|understanding | 2 | PN-2028, PN-4020 |
| nimbus|curiosity_experiment|feelings|acceptance | 2 | PN-3004, PN-4011 |
| accident|accident_plain|feelings|joint_repair | 2 | PN-3005, PN-4012 |

## Accepted: formula concentration (heuristic + reviewer overrides)
| value | count | % |
| --- | ---: | ---: |
| F1 | 0 | 0.0 |
| F2 | 2 | 1.4 |
| F3 | 0 | 0.0 |
| none | 140 | 98.6 |

## Accepted: initiator / agency
| value | count | % |
| --- | ---: | ---: |
| pip | 26 | 18.3 |
| nimbus | 35 | 24.6 |
| shared | 47 | 33.1 |
| third_force | 22 | 15.5 |
| accident | 12 | 8.5 |

## Accepted: power necessity
| value | count | % |
| --- | ---: | ---: |
| essential | 30 | 21.1 |
| enhanced | 29 | 20.4 |
| optional | 15 | 10.6 |
| irrelevant | 68 | 47.9 |

## Accepted: character-based comedy
- character-based: 142 (100.0%)

## Accepted: comedy mechanisms
| value | count | % |
| --- | ---: | ---: |
| over_literal_rules | 19 | 13.4 |
| overconfidence | 18 | 12.7 |
| stubborn_commitment | 15 | 10.6 |
| excessive_preparation | 13 | 9.2 |
| dignity_maintenance | 13 | 9.2 |
| misplaced_helpfulness | 12 | 8.5 |
| forecast_irony | 9 | 6.3 |
| imitation_flattery | 8 | 5.6 |
| feelings_visible | 7 | 4.9 |
| impatience | 7 | 4.9 |
| literal_interpretation | 6 | 4.2 |
| trying_to_impress | 3 | 2.1 |
| perfectionism | 3 | 2.1 |
| fomo | 3 | 2.1 |
| competitive_escalation | 3 | 2.1 |
| hiding_mistake | 1 | 0.7 |
| social_embarrassment | 1 | 0.7 |
| role_reversal | 1 | 0.7 |

## Accepted: third force
| value | count | % |
| --- | ---: | ---: |
| care_receiver | 28 | 19.7 |
| deadline | 6 | 4.2 |
| discovery | 9 | 6.3 |
| none | 44 | 31.0 |
| request | 16 | 11.3 |
| responsive_world | 27 | 19.0 |
| social_pressure | 12 | 8.5 |
| visitor | 0 | 0.0 |

## Accepted: resolution types
| value | count | % |
| --- | ---: | ---: |
| acceptance | 22 | 15.5 |
| compromise | 12 | 8.5 |
| help_arrives | 0 | 0.0 |
| joint_repair | 12 | 8.5 |
| reframe | 36 | 25.4 |
| reset_routine | 5 | 3.5 |
| understanding | 55 | 38.7 |

## Accepted: production burden
| value | count | % |
| --- | ---: | ---: |
| LOW | 6 | 4.2 |
| MEDIUM | 83 | 58.5 |
| HIGH | 43 | 30.3 |
| EXTREME | 10 | 7.0 |

## Burden vs quality (accepted)
| burden | n | mean review total (4-12) |
| --- | ---: | ---: |
| LOW | 6 | 9.50 |
| MEDIUM | 83 | 9.93 |
| HIGH | 43 | 9.93 |
| EXTREME | 10 | 10.20 |

## Burden vs power role (accepted)
| power role | LOW | MEDIUM | HIGH | EXTREME |
| --- | ---: | ---: | ---: | ---: |
| essential | 0 | 8 | 16 | 6 |
| enhanced | 1 | 17 | 11 | 0 |
| optional | 2 | 10 | 2 | 1 |
| irrelevant | 3 | 48 | 14 | 3 |

## Accepted: age risk flags
| value | count | % |
| --- | ---: | ---: |
| abstract_inference | 18 | 12.7 |

## Accepted: score distribution
| value | count | % |
| --- | ---: | ---: |
| 10 | 45 | 31.7 |
| 9 | 44 | 31.0 |
| 11 | 36 | 25.4 |
| 8 | 9 | 6.3 |
| 12 | 8 | 5.6 |

