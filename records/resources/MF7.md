---
records:
    - id: MF7NCSM7KX
      kind: problem-set
      title: KöMaL Problems in Mathematics, December 2009
      creators:
        - name: KöMaL editorial board
          role: editor
      date: 2009-12
      msc:
        - code: 00A07
          from: komal
        - code: 97U40
          from: komal
      expressions:
        - key: e1
          kind: edition
          language: en
          date: 2009-12
          structure: MF7NCSM7KX/e1.json
      relations:
        - kind: part_of
          to: 4T7QDPBW1N
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: komal
          snapshot: blake3:3658e660acc064da2c1a894c81d6f74fed1bee98fd8e0b9c468109c4c7e40452
          native_id: 2009-12
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: MF7XEPN4GV
      kind: preprint
      title: 'Certified Bayesian optimal experimental design: from Expected Information Gain to Signal-to-Noise Ratio'
      creators:
        - name: Mohamed Doumbouya
          role: author
        - name: Arthur Vidard
          role: author
        - name: Olivier Zahm
          role: author
      date: "2026-09-26"
      subjects:
        - system: arxiv
          code: cs.IT
        - system: arxiv
          code: math.IT
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-09-26"
          ids:
            arxiv: "2609.32282"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.32282"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2609.32282"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
