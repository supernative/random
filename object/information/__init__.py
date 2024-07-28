# Information processing cores available through this module.
# Import this as subsystem of standard object programming.

"""
Notes on different core types:
- mid-side processor
- left-right processor
- master-slave processor

• mid-side processors have encoder and decoder:
- encode : stereo image -> unit state
- decode : unit state -> stereo image

• left-right processors have encoder and decoder:
- encode : unit state -> stereo image
- decode : stereo image -> unit state

• master-slave processors have selector, embedder and sampler:
- select : master bus | slaves -> main bus
- embed : channel bus | main bus -> slaves
- sampler : master bus | slaves -> channel state
"""

data = [] # this stacks all the attention heads
image = buffer(data) # stores the intermediate representations
console = build(data, image) # master processing core that runs in parallel
blocks = console.get_discrete_samplers(k) # parallel lines that could be processes independently
operators = console.get_callbacks(blocks) # individual return path managers

status = send_for_mastering(operators, blocks)
if status:
    status = represent_to_user(image)
if status:
    status = confirm_via_user(status)

statistics = constructor.get_expectation(image)
model.set_expectation(statistics)
status = trainer.enroll(model, statistics.max())
if status:
    status = measurer.evaluate(model, statistics)
if status:
    status = generator.predict(image, maximum_length)
if status:
    ..



