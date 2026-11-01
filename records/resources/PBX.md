---
records:
    - id: PBX05QBXHP
      kind: monograph
      title: Non-Riemannian Geometry
      creators:
        - name: L. Eisenhart
          role: author
      date: "1927-12-31"
      msc:
        - code: 53-01
          from: zbmath_search
        - code: 53Cxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1927-12-31"
          ids:
            doi: 10.1090/coll/008
            zbl_id: "2588267"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1927-12-31"
              ids:
                isbn:
                    - "9780821810088"
                    - "9780821874455"
                    - "9781470431587"
              access:
                class: record
      relations:
        - kind: part_of
          to: W1VWARV4XH
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/coll/008
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "2588267"
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
    - id: PBX6AMPVT2
      kind: preprint
      title: Asymptotically Optimal Mixed-State Cloning
      creators:
        - name: Jiani Fei
          role: author
        - name: Jinzhao Wang
          role: author
      date: "2026-09-28"
      subjects:
        - system: arxiv
          code: quant-ph
        - system: arxiv
          code: math-ph
        - system: arxiv
          code: math.MP
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-28"
          ids:
            arxiv: "2609.35986"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.35986"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
---
