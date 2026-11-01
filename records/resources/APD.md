---
records:
    - id: APD7Q94ESM
      kind: problem-set
      title: Kvant 1986, no. 10
      creators:
        - name: Kvant editorial board
          role: editor
      date: "1986"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1986"
          structure: APD7Q94ESM/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1986-10
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
    - id: APD8GE0E4F
      kind: preprint
      title: On Enriched Categories and Induced Representations
      creators:
        - name: Joshua A. Leslie
          role: author
        - name: Ralph A. Twum
          role: author
      date: "2021-08-01"
      msc:
        - code: 18-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.CT
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2021-08-01"
          ids:
            arxiv: "2108.00412"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2108.00412"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2108.00412"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
