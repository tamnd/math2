---
records:
    - id: CHSB1TGAKB
      kind: preprint
      title: Lower Bounds for Linear-Oracle Online Learning
      creators:
        - name: Mohit Sinha
          role: author
      date: "2026-09-29"
      subjects:
        - system: arxiv
          code: stat.ML
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-29"
          ids:
            arxiv: "2609.38375"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.38375"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: CHSYPWGM16
      kind: monograph
      title: Special Functions, Probability Semigroups, and Hamiltonian Flows
      creators:
        - name: Philip J. Feinsilver
          role: author
      date: "1978"
      msc:
        - code: 33-02
          from: zbmath_search
        - code: 60J35
          from: zbmath_search
        - code: 60H05
          from: zbmath_search
        - code: 81R10
          from: zbmath_search
        - code: 47D03
          from: zbmath_search
        - code: 44A45
          from: zbmath_search
        - code: 33C05
          from: zbmath_search
        - code: 33C45
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1978"
          ids:
            doi: 10.1007/bfb0064532
            zbl: "0394.33002"
            zbl_id: "3611702"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1978"
              ids:
                isbn:
                    - "9783540091004"
                    - "9783540355540"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0064532
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3611702"
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
---
