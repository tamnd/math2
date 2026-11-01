---
records:
    - id: Z2M0ZZNJKM
      kind: monograph
      title: 'Markov Chains: Gibbs Fields, Monte Carlo Simulation, and Queues'
      creators:
        - name: Pierre Brémaud
          role: author
      date: "1999"
      msc:
        - code: 60-02
          from: zbmath_search
        - code: 60J10
          from: zbmath_search
        - code: 60G60
          from: zbmath_search
        - code: 60J27
          from: zbmath_search
        - code: 60K10
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1999"
          ids:
            doi:
                - 10.1007/978-1-4757-3124-8
                - 10.1007/978-3-030-45982-6
            zbl: "0949.60009"
            zbl_id: "1313673"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1999"
              ids:
                isbn:
                    - "9781441931313"
                    - "9781475731248"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2020"
              ids:
                isbn:
                    - "9783030459819"
                    - "9783030459826"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7B8JKAVW9F
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-3124-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-45982-6
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "1313673"
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
    - id: Z2M4D55R57
      kind: preprint
      title: 'Learn Feasibility Once, Optimize All Objectives: Derivative-Free Diffusion Models for Chance-Constrained Programming'
      creators:
        - name: Ziwen Liu
          role: author
        - name: Yan Liu
          role: author
        - name: Congying Han
          role: author
        - name: Tiande Guo
          role: author
        - name: Yao Yan
          role: author
        - name: Weichen Zhao
          role: author
      date: "2026-10-02"
      subjects:
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-02"
          ids:
            arxiv: "2610.03071"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.03071"
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
