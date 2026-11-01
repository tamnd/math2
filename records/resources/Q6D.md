---
records:
    - id: Q6DHV77M7J
      kind: problem-set
      title: IMO 2016
      creators:
        - name: IMO Problem Selection Committee
          role: author
      date: "2016"
      msc:
        - code: 00A07
          from: imo
        - code: 97U40
          from: imo
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2016"
      relations:
        - kind: part_of
          to: 931689K6X2
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: imo
          snapshot: blake3:c564548c1a7c5bfe4e71cf81d61c599a9d4016d698feff8fb0bc9beb0e2f88f9
          native_id: "2016"
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
    - id: Q6DX43KXJ0
      kind: monograph
      title: 'Solving Problems in Mathematical Analysis, Part III: Curves and Surfaces, Conditional Extremes, Curvilinear Integrals, Complex Functions, Singularities and Fourier Series'
      creators:
        - name: Tomasz Radożycki
          role: author
      date: "2020"
      msc:
        - code: 26-01
          from: zbmath_search
        - code: 30-01
          from: zbmath_search
        - code: 42-01
          from: zbmath_search
        - code: 58-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2020"
          ids:
            doi: 10.1007/978-3-030-38596-5
            zbl: "1439.26006"
            zbl_id: "7183912"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2020"
              ids:
                isbn:
                    - "9783030385958"
                    - "9783030385965"
              access:
                class: record
      relations:
        - kind: part_of
          to: AQAR17SPHM
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-38596-5
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "7183912"
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
