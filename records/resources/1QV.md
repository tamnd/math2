---
records:
    - id: 1QVKNGBS3D
      kind: preprint
      title: Multi-Agent Reinforcement Learning via Double Averaging Primal-Dual Optimization
      creators:
        - name: Hoi-To Wai
          role: author
        - name: Zhuoran Yang
          role: author
        - name: Zhaoran Wang
          role: author
        - name: Mingyi Hong
          role: author
      date: "2018-06-03"
      subjects:
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.OC
        - system: arxiv
          code: stat.ML
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2018-06-03"
          ids:
            arxiv: "1806.00877"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.17 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "1806.00877"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: 1QVSBDQY15
      kind: monograph
      title: Automorphic Forms on GL (3,ℝ)
      creators:
        - name: Daniel Bump
          role: author
      date: "1984"
      msc:
        - code: "22E30"
          from: zbmath_search
        - code: 22-02
          from: zbmath_search
        - code: 11-02
          from: zbmath_search
        - code: 11F70
          from: zbmath_search
        - code: 11F67
          from: zbmath_search
        - code: 11F12
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1984"
          ids:
            doi: 10.1007/bfb0100147
            zbl: "0543.22005"
            zbl_id: "3863503"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1984"
              ids:
                isbn:
                    - "9783540138648"
                    - "9783540390558"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.17 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0100147
          level: work
        - source: zbmath_search
          snapshot: blake3:ba52b67aca79888bd54f4ac0d57bd446df8c82ca03dd9e92e0bc9db1402905ce
          native_id: "3863503"
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
          at: "2026-11-02"
          by: m2 v0.6.17 scope/1
          note: from in to in
---
