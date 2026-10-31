---
records:
    - id: XFZFR84KTZ
      kind: problem-set
      title: IMO 1960
      date: "1960"
      expressions:
        - key: e1
          kind: edition
          date: "1960"
      relations:
        - kind: part_of
          to: 931689K6X2
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: imo
          snapshot: blake3:c564548c1a7c5bfe4e71cf81d61c599a9d4016d698feff8fb0bc9beb0e2f88f9
          native_id: "1960"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: XFZJZS3GB1
      kind: preprint
      title: Pipelined Gradient Coding
      creators:
        - name: Xian Su
          role: author
        - name: Jun Li
          role: author
      date: "2026-07-22"
      msc:
        - code: 94-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: cs.IT
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.IT
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-07-22"
          ids:
            arxiv: "2607.20739"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2607.20739"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2607.20739"
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
