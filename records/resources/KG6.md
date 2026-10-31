---
records:
    - id: KG6ABR832E
      kind: monograph
      title: What is the Genus?
      creators:
        - name: Patrick Popescu-Pampu
          role: author
      date: "2016"
      expressions:
        - key: e1
          kind: edition
          date: "2016"
          ids:
            doi: 10.1007/978-3-319-42312-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2016"
              ids:
                isbn:
                    - "9783319423111"
                    - "9783319423128"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-42312-8
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: KG6V5AN3PK
      kind: preprint
      title: Off-diagonal bounds for spectral projector kernels
      creators:
        - name: Panagiotis Dimakis
          role: author
      date: "2026-09-27"
      msc:
        - code: 35-XX
          from: arxiv
        - code: 47-XX
          from: arxiv
        - code: 58-XX
          from: arxiv
        - code: 26-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.SP
        - system: arxiv
          code: math.AP
        - system: arxiv
          code: math.CA
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2026-09-27"
          ids:
            arxiv: "2609.33957"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.33957"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2609.33957"
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
