#action.yaml
name: 'custom GitHub Action'
description: 'A GitHub Action that takes an inpt and returns the square of the number'
inputs:
  num:
    description: 'Enter a number'
    required: true
    default: "1"
outputs:
  num_squared:
    descripion: "square of the input"
    # need to specify the extra 'value' field for 'composite' actions
    value: ${{ steps.get.square.outpts.num_squared }}
runs:
  using: 'composite'
  steps:
    -name: Insall Dependencies
     run: pip install -r requrements.tx
     shell: bash
    -name: Pass Inpus to Shell
     run: |
       echo "INPUT_NUM=${{ inpus.num }}" >> $GITHUB_ENV
     shell: bash
    -name: Fetch the number's squae
     id: get-square
     run: python src/get_num_square.py
     shell: bash
