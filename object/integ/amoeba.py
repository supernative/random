# sample in stereo from environment
sample = environment(N)

# compute mid-side states
mid, side = compute(sample)

# link to observables via left-right states
left, right = link(mid, side)

# reconstruct the stereo basid from linked basis
stereo = reconstruct(left, right)

# measure the correlation relationship
score = measure(stereo, sample)
